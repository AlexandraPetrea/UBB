#include"pch.h"
#include "lodepng.h"
#include <iostream>
#include <thread>
#include <mpi.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <chrono>

struct raw_image {
	std::vector<unsigned char> img;
	unsigned width, height;
};

struct image {
	std::vector<std::vector<float>>red;
	std::vector<std::vector<float>>green;
	std::vector<std::vector<float>>blue;
	std::vector<std::vector<float>>alpha;
};

struct acumulator {
	float red = 0;
	float green = 0;
	float blue = 0;
};

//float filter[3][3] = { {1.0 / 16.0, 2.0 / 16.0, 1.0 / 16.0 }, { 2.0 / 16.0, 4.0 / 16.0, 2.0 / 16.0 }, { 1.0 / 16.0, 2.0 / 16.0, 1.0 / 16.0 } };
//float filter[3][3] = { {0.0, -1.0, 0.0 }, { -1.0, 5.0, -1.0 }, { 0.0, -1.0, 0.0 } };
float filter[3][3] = { {1.0 / 9.0, 1.0 / 9.0, 1.0 / 9.0 },{1.0 / 9.0, 1.0 / 9.0, 1.0 / 9.0 }, {1.0 / 9.0, 1.0 / 9.0, 1.0 / 9.0 } };

int height;
int width;
int procId;
int nrProcs;

raw_image decodeOneStep(const char* filename) {
	std::cout << "Loading image " << filename << "..." << std::endl;
	std::vector<unsigned char> img; //the raw pixels
	unsigned width, height;
	unsigned error = lodepng::decode(img, width, height, filename);
	if (error) std::cout << "decoder error " << error << ": " << lodepng_error_text(error) << std::endl;
	std::cout << "Image loaded!" << std::endl;
	return raw_image{ img, width, height };
}

void encodeOneStep(const char* filename, raw_image inputImg) {
	std::cout << "Writing image..." << std::endl;
	unsigned error = lodepng::encode(filename, inputImg.img, inputImg.width, inputImg.height);
	if (error) std::cout << "encoder error " << error << ": " << lodepng_error_text(error) << std::endl;
	std::cout << "Image written!" << std::endl;;
}

image raw_to_image(raw_image img) {
	image new_image;
	int k = 0;
	for (int i = 0; i < (signed)img.height; i++) {
		new_image.red.push_back(std::vector<float>());
		new_image.green.push_back(std::vector<float>());
		new_image.blue.push_back(std::vector<float>());
		new_image.alpha.push_back(std::vector<float>());

		for (int j = 0; j < (signed)img.width; j++) {
			new_image.red[i].push_back(img.img[k]);
			new_image.green[i].push_back(img.img[k + 1]);
			new_image.blue[i].push_back(img.img[k + 2]);
			new_image.alpha[i].push_back(img.img[k + 3]);
			k += 4;
		}
	}
	return new_image;
}

raw_image image_to_raw(image img) {
	raw_image new_image;
	new_image.height = img.red.size();
	new_image.width = img.red[0].size();
	for (int i = 0; i < (signed)img.red.size(); i++) {
		for (int j = 0; j < (signed)img.red[0].size(); j++) {
			new_image.img.push_back((unsigned char)img.red[i][j]);
			new_image.img.push_back((unsigned char)img.green[i][j]);
			new_image.img.push_back((unsigned char)img.blue[i][j]);
			new_image.img.push_back((unsigned char)img.alpha[i][j]);
		}
	}
	return new_image;
}

image make_new_image(int width, int height) {
	image img;
	for (int i = 0; i < height; i++) {
		img.red.push_back(std::vector<float>(width, 0));
		img.green.push_back(std::vector<float>(width, 0));
		img.blue.push_back(std::vector<float>(width, 0));
		img.alpha.push_back(std::vector<float>(width, 0));
	}
	return img;
}

image master(raw_image inputImage) {
	MPI_Status status;
	std::cout << "Master started...\n";
	image img = raw_to_image(inputImage);
	height = img.red.size();
	width = img.red[0].size();

	image outputImage = make_new_image(width, height);

	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int size = inputImage.width * inputImage.height;
	for (int i = 1; i < nrProcs; i++) {
		int begin = size * i / nrProcs;
		int end = size * (i + 1) / nrProcs;
		MPI_Send(&begin, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
		MPI_Send(&end, 1, MPI_INT, i, 2, MPI_COMM_WORLD);
	}

	std::cout << "Finished sending info to children...\n";

	if (nrProcs > 1) {
		for (int i = 0; i < height; i++) {
			MPI_Bcast(img.red[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.green[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.blue[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.alpha[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		}

		std::cout << "Finished bcasting input image to children\n";
	}

	for (int i = 0; i < size / nrProcs; i++) {
		int y = i / height;
		int x = i % width;

		acumulator a;
		for (int h = -1; h < 2; h++) {
			if (h + y < 0 || h + y >= height)
				continue;
			for (int w = -1; w < 2; w++) {
				if (w + x < 0 || w + x >= width)
					continue;

				a.red += img.red[y + h][x + w] * filter[h + 1][w + 1];
				a.green += img.green[y + h][x + w] * filter[h + 1][w + 1];
				a.blue += img.blue[y + h][x + w] * filter[h + 1][w + 1];
			}
		}
		outputImage.red[y][x] = a.red;
		outputImage.green[y][x] = a.green;
		outputImage.blue[y][x] = a.blue;
		outputImage.alpha[y][x] = img.alpha[y][x];
	}

	std::cout << "Master finished processing...\n";

	std::vector<float> r(width);
	std::vector<float> g(width);
	std::vector<float> b(width);
	std::vector<float> a(width);

	for (int i = 1; i < nrProcs; i++) {
		for (int j = 0; j < height; j++) {
			MPI_Recv(r.data(), width, MPI_FLOAT, i, 3, MPI_COMM_WORLD, &status);
			MPI_Recv(g.data(), width, MPI_FLOAT, i, 4, MPI_COMM_WORLD, &status);
			MPI_Recv(b.data(), width, MPI_FLOAT, i, 5, MPI_COMM_WORLD, &status);
			MPI_Recv(a.data(), width, MPI_FLOAT, i, 6, MPI_COMM_WORLD, &status);

			for (int k = 0; k < width; k++) {
				outputImage.red[j][k] += r[k];
				outputImage.green[j][k] += g[k];
				outputImage.blue[j][k] += b[k];
				outputImage.alpha[j][k] += a[k];
			}
		}
	}

	std::cout << "Master finished receiving from slave...\n";
	return outputImage;
}

void slave() {
	MPI_Status status;
	std::cout << "Slave " << procId << " started...\n";

	int width, height;
	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	std::cout << "slave " << procId << " received image sizes...\n";

	int begin, end;
	MPI_Recv(&begin, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
	MPI_Recv(&end, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, &status);

	image img;
	image outputImage = make_new_image(width, height);


	for (int i = 0; i < height; i++) {
		std::vector<float> tmp(width);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.red.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.green.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.blue.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.alpha.push_back(tmp);
	}

	std::cout << "Slave " << procId << " received input image...\n";

	for (int i = begin; i < end; i++) {
		int y = i / height;
		int x = i % width;

		acumulator a;
		for (int h = -1; h < 2; h++) {
			if (h + y < 0 || h + y >= height)
				continue;
			for (int w = -1; w < 2; w++) {
				if (w + x < 0 || w + x >= width)
					continue;

				a.red += img.red[y + h][x + w] * filter[h + 1][w + 1];
				a.green += img.green[y + h][x + w] * filter[h + 1][w + 1];
				a.blue += img.blue[y + h][x + w] * filter[h + 1][w + 1];
			}
		}
		outputImage.red[y][x] = a.red;
		outputImage.green[y][x] = a.green;
		outputImage.blue[y][x] = a.blue;
		outputImage.alpha[y][x] = img.alpha[y][x];
	}

	for (int i = 0; i < height; i++) {
		MPI_Send(outputImage.red[i].data(), width, MPI_FLOAT, 0, 3, MPI_COMM_WORLD);
		MPI_Send(outputImage.green[i].data(), width, MPI_FLOAT, 0, 4, MPI_COMM_WORLD);
		MPI_Send(outputImage.blue[i].data(), width, MPI_FLOAT, 0, 5, MPI_COMM_WORLD);
		MPI_Send(outputImage.alpha[i].data(), width, MPI_FLOAT, 0, 6, MPI_COMM_WORLD);
	}

	std::cout << "Slave " << procId << " finished\n";

}

image masterContrast(raw_image inputImage) {
	MPI_Status status;
	std::cout << "Master started...\n";
	image img = raw_to_image(inputImage);
	height = img.red.size();
	width = img.red[0].size();

	image outputImage = make_new_image(width, height);

	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int size = inputImage.width * inputImage.height;
	for (int i = 1; i < nrProcs; i++) {
		int begin = size * i / nrProcs;
		int end = size * (i + 1) / nrProcs;
		MPI_Send(&begin, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
		MPI_Send(&end, 1, MPI_INT, i, 2, MPI_COMM_WORLD);
	}

	std::cout << "Finished sending info to children...\n";

	if (nrProcs > 1) {
		for (int i = 0; i < height; i++) {
			MPI_Bcast(img.red[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.green[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.blue[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.alpha[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		}

		std::cout << "Finished bcasting input image to children\n";
	}

	for (int k = 0; k < size / nrProcs; k++) {
		int i = k / height;
		int j = k % width;
		if (i == 0 || i == height - 1 || j == 0 || j == width - 1)
			continue;
		acumulator new_image;
		for (int h = -1; h < 2; h++) {
			for (int w = -1; w < 2; w++) {
				float factor = (259 * (128 + 255)) / (255 * (259 - 128));

				new_image.red = factor * (img.red[i + h][j + w] - 128) + 128;
				if (new_image.red > 255) {
					new_image.red = 255;
				}
				if (new_image.red < 0) {
					new_image.red = 0;
				}
				new_image.blue = factor * (img.blue[i + h][j + w] - 128) + 128;
				if (new_image.blue > 255) {
					new_image.blue = 255;
				}
				if (new_image.blue < 0) {
					new_image.blue = 0;
				}
				new_image.green = factor * (img.green[i + h][j + w] - 128) + 128;
				if (new_image.green > 255) {
					new_image.green = 255;
				}
				if (new_image.green < 0) {
					new_image.green = 0;
				}

			}
		}
		outputImage.red[i - 1][j - 1] = new_image.red;
		outputImage.green[i - 1][j - 1] = new_image.green;
		outputImage.blue[i - 1][j - 1] = new_image.blue;
		outputImage.alpha[i - 1][j - 1] = img.alpha[i][j];
	}

	std::cout << "Master finished processing...\n";

	std::vector<float> r(width);
	std::vector<float> g(width);
	std::vector<float> b(width);
	std::vector<float> a(width);

	for (int i = 1; i < nrProcs; i++) {
		for (int j = 0; j < height; j++) {
			MPI_Recv(r.data(), width, MPI_FLOAT, i, 3, MPI_COMM_WORLD, &status);
			MPI_Recv(g.data(), width, MPI_FLOAT, i, 4, MPI_COMM_WORLD, &status);
			MPI_Recv(b.data(), width, MPI_FLOAT, i, 5, MPI_COMM_WORLD, &status);
			MPI_Recv(a.data(), width, MPI_FLOAT, i, 6, MPI_COMM_WORLD, &status);

			for (int k = 0; k < width; k++) {
				outputImage.red[j][k] += r[k];
				outputImage.green[j][k] += g[k];
				outputImage.blue[j][k] += b[k];
				outputImage.alpha[j][k] += a[k];
			}
		}
	}

	std::cout << "Master finished receiving from slave...\n";
	return outputImage;
}

void slaveContrast() {
	MPI_Status status;
	std::cout << "Slave " << procId << " started...\n";

	int width, height;
	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	std::cout << "slave " << procId << " received image sizes...\n";

	int begin, end;
	MPI_Recv(&begin, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
	MPI_Recv(&end, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, &status);

	image img;
	image outputImage = make_new_image(width, height);


	for (int i = 0; i < height; i++) {
		std::vector<float> tmp(width);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.red.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.green.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.blue.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.alpha.push_back(tmp);
	}

	std::cout << "Slave " << procId << " received input image...\n";

	int i = 0;
	int j = 0;
	for (int k = begin; k < end; k++) {
		i = k / height;
		j = k % width;
		if (i == 0 || i == height - 1 || j == 0 || j == width - 1)
			continue;
		acumulator new_image;
		for (int h = -1; h < 2; h++) {
			for (int w = -1; w < 2; w++) {
				float factor = (259 * (128 + 255)) / (255 * (259 - 128));

				new_image.red = factor * (img.red[i + h][j + w] - 128) + 128;
				if (new_image.red > 255) {
					new_image.red = 255;
				}
				if (new_image.red < 0) {
					new_image.red = 0;
				}
				new_image.blue = factor * (img.blue[i + h][j + w] - 128) + 128;
				if (new_image.blue > 255) {
					new_image.blue = 255;
				}
				if (new_image.blue < 0) {
					new_image.blue = 0;
				}
				new_image.green = factor * (img.green[i + h][j + w] - 128) + 128;
				if (new_image.green > 255) {
					new_image.green = 255;
				}
				if (new_image.green < 0) {
					new_image.green = 0;
				}

			}
		}
		outputImage.red[i - 1][j - 1] = new_image.red;
		outputImage.green[i - 1][j - 1] = new_image.green;
		outputImage.blue[i - 1][j - 1] = new_image.blue;
		outputImage.alpha[i - 1][j - 1] = img.alpha[i][j];
	}

	for (int i = 0; i < height; i++) {
		MPI_Send(outputImage.red[i].data(), width, MPI_FLOAT, 0, 3, MPI_COMM_WORLD);
		MPI_Send(outputImage.green[i].data(), width, MPI_FLOAT, 0, 4, MPI_COMM_WORLD);
		MPI_Send(outputImage.blue[i].data(), width, MPI_FLOAT, 0, 5, MPI_COMM_WORLD);
		MPI_Send(outputImage.alpha[i].data(), width, MPI_FLOAT, 0, 6, MPI_COMM_WORLD);
	}

	std::cout << "Slave " << procId << " finished\n";

}

image masterGrayscale(raw_image inputImage) {
	MPI_Status status;
	std::cout << "Master started...\n";
	image img = raw_to_image(inputImage);
	height = img.red.size();
	width = img.red[0].size();

	image outputImage = make_new_image(width, height);

	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	int size = inputImage.width * inputImage.height;
	for (int i = 1; i < nrProcs; i++) {
		int begin = size * i / nrProcs;
		int end = size * (i + 1) / nrProcs;
		MPI_Send(&begin, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
		MPI_Send(&end, 1, MPI_INT, i, 2, MPI_COMM_WORLD);
	}

	std::cout << "Finished sending info to children...\n";

	if (nrProcs > 1) {
		for (int i = 0; i < height; i++) {
			MPI_Bcast(img.red[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.green[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.blue[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
			MPI_Bcast(img.alpha[i].data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		}

		std::cout << "Finished bcasting input image to children\n";
	}

	for (int k = 0; k < size / nrProcs; k++) {
		int i = k / height;
		int j = k % width;
		if (i == 0 || i == height - 1 || j == 0 || j == width - 1)
			continue;
		acumulator a;
		for (int h = -1; h < 2; h++) {
			for (int w = -1; w < 2; w++) {
				int sum = (int)(img.red[i + h][j + w] * 0.299 + img.green[i + h][j + w] * 0.587 + img.blue[i + h][j + w] * 0.114);
				if (sum > 255)
					a.red = 255, a.green = 255, a.blue = 255;
				else
					a.red = sum, a.green = sum, a.blue = sum;
			}
		}
		outputImage.red[i - 1][j - 1] = a.red;
		outputImage.green[i - 1][j - 1] = a.green;
		outputImage.blue[i - 1][j - 1] = a.blue;
		outputImage.alpha[i - 1][j - 1] = img.alpha[i][j];
	}

	std::cout << "Master finished processing...\n";

	std::vector<float> r(width);
	std::vector<float> g(width);
	std::vector<float> b(width);
	std::vector<float> a(width);

	for (int i = 1; i < nrProcs; i++) {
		for (int j = 0; j < height; j++) {
			MPI_Recv(r.data(), width, MPI_FLOAT, i, 3, MPI_COMM_WORLD, &status);
			MPI_Recv(g.data(), width, MPI_FLOAT, i, 4, MPI_COMM_WORLD, &status);
			MPI_Recv(b.data(), width, MPI_FLOAT, i, 5, MPI_COMM_WORLD, &status);
			MPI_Recv(a.data(), width, MPI_FLOAT, i, 6, MPI_COMM_WORLD, &status);

			for (int k = 0; k < width; k++) {
				outputImage.red[j][k] += r[k];
				outputImage.green[j][k] += g[k];
				outputImage.blue[j][k] += b[k];
				outputImage.alpha[j][k] += a[k];
			}
		}
	}

	std::cout << "Master finished receiving from slave...\n";
	return outputImage;
}

void slaveGrayscale() {
	MPI_Status status;
	std::cout << "Slave " << procId << " started...\n";

	int width, height;
	MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);
	MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);

	std::cout << "slave " << procId << " received image sizes...\n";

	int begin, end;
	MPI_Recv(&begin, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);
	MPI_Recv(&end, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, &status);

	image img;
	image outputImage = make_new_image(width, height);


	for (int i = 0; i < height; i++) {
		std::vector<float> tmp(width);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.red.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.green.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.blue.push_back(tmp);
		MPI_Bcast(tmp.data(), width, MPI_FLOAT, 0, MPI_COMM_WORLD);
		img.alpha.push_back(tmp);
	}

	std::cout << "Slave " << procId << " received input image...\n";

	for (int k = begin; k < end; k++) {
		int i = k / height;
		int j = k % width;
		if (i == 0 || i == height - 1 || j == 0 || j == width - 1)
			continue;
		acumulator a;
		for (int h = -1; h < 2; h++) {
			for (int w = -1; w < 2; w++) {
				int sum = (int)(img.red[i + h][j + w] * 0.299 + img.green[i + h][j + w] * 0.587 + img.blue[i + h][j + w] * 0.114);
				if (sum > 255)
					a.red = 255, a.green = 255, a.blue = 255;
				else
					a.red = sum, a.green = sum, a.blue = sum;
			}
		}
		outputImage.red[i - 1][j - 1] = a.red;
		outputImage.green[i - 1][j - 1] = a.green;
		outputImage.blue[i - 1][j - 1] = a.blue;
		outputImage.alpha[i - 1][j - 1] = img.alpha[i][j];
	}

	for (int i = 0; i < height; i++) {
		MPI_Send(outputImage.red[i].data(), width, MPI_FLOAT, 0, 3, MPI_COMM_WORLD);
		MPI_Send(outputImage.green[i].data(), width, MPI_FLOAT, 0, 4, MPI_COMM_WORLD);
		MPI_Send(outputImage.blue[i].data(), width, MPI_FLOAT, 0, 5, MPI_COMM_WORLD);
		MPI_Send(outputImage.alpha[i].data(), width, MPI_FLOAT, 0, 6, MPI_COMM_WORLD);
	}

	std::cout << "Slave " << procId << " finished\n";

}


int main(int argc, char *argv[]) {
	MPI_Init(NULL, NULL);
	MPI_Comm_rank(MPI_COMM_WORLD, &procId);
	MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);

	if (procId == 0) {
		const char* fileName;
		if (argc != 2) {
			fileName = "lenna.png";
		}
		else {
			fileName = argv[1];
		}

		raw_image inputImage;
		image processedImage;
		inputImage = decodeOneStep(fileName);
		/*
		//Blur..
		auto start = std::chrono::system_clock::now();
		processedImage = master(inputImage);
		auto stop = std::chrono::system_clock::now();
		std::chrono::duration<double> elapsed_seconds = stop - start;
		//cout << "nr processes" << nrProcs << "\n";
		std::cout << "Blur time = " << elapsed_seconds.count() * 1000 << " ms\n";
		encodeOneStep("output.png", image_to_raw(processedImage));
		*/
		
		//Grayscale...
		auto start = std::chrono::system_clock::now();
		processedImage = masterGrayscale(inputImage);
		auto stop = std::chrono::system_clock::now();
		std::chrono::duration<double> elapsed_seconds = stop - start;
		//cout << "nr processes" << nrProcs << "\n";
		std::cout << "Grayscale time = " << elapsed_seconds.count() * 1000 << " ms\n";
		encodeOneStep("outputGrasycale.png", image_to_raw(processedImage));
		
		/*
		//Contrast..'
		auto start = std::chrono::system_clock::now();
		processedImage = masterContrast(inputImage);
		auto stop = std::chrono::system_clock::now();
		std::chrono::duration<double> elapsed_seconds = stop - start;
		//cout << "nr processes" << nrProcs << "\n";
		std::cout << "Contrast time = " << elapsed_seconds.count() * 1000 << " ms\n";
		encodeOneStep("outputContrast.png", image_to_raw(processedImage));
		*/
	}
	else {
		//slave();
		slaveGrayscale();
		//slaveContrast();

	}

	MPI_Finalize();
	return 0;
}
