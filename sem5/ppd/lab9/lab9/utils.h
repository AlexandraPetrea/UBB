#ifndef PDP_PROJECT_UTILS_
#define PDP_PROJECT_UTILS_

#include <Magick++.h>
#include <mpi.h>

#include "matrix.h"

template<typename T>
struct RgbMatrix {
	RgbMatrix(int h, int w) :
		height(h), width(w), red(h, w), green(h, w), blue(h, w) {}

	int height, width;
	Matrix<T> red;
	Matrix<T> green;
	Matrix<T> blue;
};


RgbMatrix<int> ImageToRgbMatrix(const Magick::Image& image) {
	const int h = image.rows();
	const int w = image.columns();

	RgbMatrix<int> matrix(h, w);

	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			Magick::Color color = image.pixelColor(j, i);
			const int rvalue = color.quantumRed() * 1LL * 255 / QuantumRange;
			const int gvalue = color.quantumGreen() * 1LL * 255 / QuantumRange;
			const int bvalue = color.quantumBlue() * 1LL * 255 / QuantumRange;
			matrix.red[i][j] = rvalue;
			matrix.green[i][j] = gvalue;
			matrix.blue[i][j] = bvalue;
		}
	}

	return matrix;
}


Magick::Image RgbMatrixToImage(const RgbMatrix<int>& matrix) {
	const int h = matrix.height;
	const int w = matrix.width;

	Magick::Image image(Magick::Geometry(w, h), "white");

	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			const int rvalue = matrix.red[i][j] * 1LL * QuantumRange / 255;
			const int gvalue = matrix.green[i][j] * 1LL * QuantumRange / 255;
			const int bvalue = matrix.blue[i][j] * 1LL * QuantumRange / 255;
			Magick::Color color(rvalue, gvalue, bvalue);
			image.pixelColor(j, i, color);
		}
	}
	return image;
}

RgbMatrix<int> Crop(const RgbMatrix<int>& matrix, int x0, int y0, int x1,
	int y1) {
	const int h = x1 - x0;
	const int w = y1 - y0;
	RgbMatrix<int> output(h, w);
	output.red = matrix.red.crop(x0, y0, x1, y1);
	output.green = matrix.green.crop(x0, y0, x1, y1);
	output.blue = matrix.blue.crop(x0, y0, x1, y1);
	return output;
}

void Expand(const RgbMatrix<int>& new_matrix, RgbMatrix<int>* old_matrix) {
	old_matrix->red.expand(new_matrix.red);
	old_matrix->green.expand(new_matrix.green);
	old_matrix->blue.expand(new_matrix.blue);
	old_matrix->height += new_matrix.height;
}


void MPI_RecvVector(std::vector<int>* vector, int source) {
	MPI_Status status;

	int num_elements;
	int* elements;
	MPI_Recv(&num_elements, 1, MPI_INT, source, MPI_ANY_TAG, MPI_COMM_WORLD,
		&status);

	elements = new int[num_elements];
	MPI_Recv(elements, num_elements, MPI_INT, source, MPI_ANY_TAG, MPI_COMM_WORLD,
		&status);

	*vector = std::vector<int>(elements, elements + num_elements);

	delete elements;
}


void MPI_SendVector(const std::vector<int>& vector, int destination) {
	int num_elements = vector.size();
	const int* elements = vector.data();
	MPI_Send(&num_elements, 1, MPI_INT, destination, 123, MPI_COMM_WORLD);
	MPI_Send(elements, num_elements, MPI_INT, destination, 123, MPI_COMM_WORLD);
}


void MPI_RecvMatrix(Matrix<int>* matrix, int source) {
	MPI_Status status;

	int height;
	int width;
	MPI_Recv(&height, 1, MPI_INT, source, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
	MPI_Recv(&width, 1, MPI_INT, source, MPI_ANY_TAG, MPI_COMM_WORLD, &status);

	std::vector<std::vector<int>> rows(height, std::vector<int>(width, 0));

	for (int i = 0; i < height; ++i) {
		MPI_RecvVector(&rows[i], source);
	}

	(*matrix) = Matrix<int>(rows);
}


void MPI_SendMatrix(const Matrix<int>& matrix, int destination) {
	int height = matrix.h();
	int width = matrix.w();
	MPI_Send(&height, 1, MPI_INT, destination, 123, MPI_COMM_WORLD);
	MPI_Send(&width, 1, MPI_INT, destination, 123, MPI_COMM_WORLD);
	for (int i = 0; i < height; ++i) {
		MPI_SendVector(matrix[i], destination);
	}
}


void MPI_RecvRgbMatrix(RgbMatrix<int>* rgb_matrix, int source) {
	MPI_RecvMatrix(&rgb_matrix->red, source);
	MPI_RecvMatrix(&rgb_matrix->green, source);
	MPI_RecvMatrix(&rgb_matrix->blue, source);
	rgb_matrix->height = rgb_matrix->red.h();
	rgb_matrix->width = rgb_matrix->red.w();
}


void MPI_SendRgbMatrix(const RgbMatrix<int>& rgb_matrix, int destination) {
	MPI_SendMatrix(rgb_matrix.red, destination);
	MPI_SendMatrix(rgb_matrix.green, destination);
	MPI_SendMatrix(rgb_matrix.blue, destination);
}


#endif  // PDP_PROJECT_UTILS_