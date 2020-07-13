#include"pch.h"
#include <iostream> 
#include <algorithm>
#include <mpi.h>
#include "kernels.h"
#include "matrix.h"
#include "utils.h"
#include <exception>   
#include <Magick++.h>

using namespace Magick;
using namespace std;

int kMe, kNumNodes;
void Master(int argc, char** argv);
void Slave();

RgbMatrix<int> Solve(const RgbMatrix<int>& input, const Matrix<int>& kernel);

int main(int argc, char** argv) {
	MPI_Init(0, 0);
	MPI_Comm_size(MPI_COMM_WORLD, &kNumNodes);
	MPI_Comm_rank(MPI_COMM_WORLD, &kMe);

	kMe ? Slave() : Master(argc, argv);

	MPI_Finalize();

	return 0;
}

void Master(int argc, char** argv) {
	if (argc <= 3) {
		fprintf(stderr,
			"usage: %s <input_image> <output_image> <kernel>\n",
			argv[0]);
		for (int i = 0; i < Kernels::num_kernels(); ++i) {
			fprintf(stderr, "kernel #%d: %s\n", i, Kernels::name(i).c_str());
		}
		exit(1);
	}

	string input_filename(argv[1]);
	string output_filename(argv[2]);
	int kernel;
	sscanf(argv[3], "%d", &kernel);

	Image input_image, output_image;
	try {
		fprintf(stderr, "Attempting to read \"%s\"... ", input_filename.c_str());
		input_image.read(input_filename);
		fprintf(stderr, "Image was read.\n");

		fprintf(stderr, "Attempting to convert image to RGB matrix... ");
		RgbMatrix<int> rgb_matrix = ImageToRgbMatrix(input_image);
		fprintf(stderr, "Conversion to RGB matrix is done.\n");

		rgb_matrix = Solve(rgb_matrix, Kernels::kernel(kernel));

		fprintf(stderr, "Attempting to convert RGB matrix to image... ");
		output_image = RgbMatrixToImage(rgb_matrix);
		fprintf(stderr, "Conversion to image is done.\n");

		fprintf(stderr, "Attempting to write to \"%s\"... ", output_filename.c_str());
		output_image.write(output_filename);
		fprintf(stderr, "Image was written.\n");

	}
	catch (exception& err) {
		cout << err.what() << endl;
		fprintf(stderr, "Some error occured.\n");
		exit(1);
	}
}

void ComputeLines(const RgbMatrix<int>& input, const Matrix<int>& kernel,
	RgbMatrix<int>* output) {
	const int overlap = kernel.h();
	for (int i = 0; i < output->height; ++i) {
		for (int j = 0; j < output->width; ++j) {
			const int x = i - kernel.h() / 2;
			const int y = j - kernel.w() / 2;
			output->red[i][j] = input.red.convolute(kernel, x, y);
			output->green[i][j] = input.green.convolute(kernel, x, y);
			output->blue[i][j] = input.blue.convolute(kernel, x, y);
		}
	}
	*output = Crop(*output, overlap, 0, output->height - overlap, output->width);
}

void Slave() {
	RgbMatrix<int> input(0, 0);
	MPI_RecvRgbMatrix(&input, 0);

	Matrix<int> kernel(0, 0);
	MPI_RecvMatrix(&kernel, 0);

	RgbMatrix<int> output(input.height, input.width);
	ComputeLines(input, kernel, &output);

	MPI_SendRgbMatrix(output, 0);
}

RgbMatrix<int> Solve(const RgbMatrix<int>& input, const Matrix<int>& kernel) {
	const int lines_per_node = input.height / kNumNodes + (input.height % kNumNodes
		!= 0);
	const int overlap = kernel.h();

	for (int i = 1; i < kNumNodes; ++i) {
		const int x0 = i * lines_per_node - overlap;
		const int y0 = 0;
		const int x1 = min(input.height, (i + 1) * lines_per_node) + overlap;
		const int y1 = input.width;
		MPI_SendRgbMatrix(Crop(input, x0, y0, x1, y1), i);
		MPI_SendMatrix(kernel, i);
	}

	RgbMatrix<int> output(min(input.height, lines_per_node), input.width);
	{
		const int x0 = -overlap;
		const int y0 = 0;
		const int x1 = min(input.height, lines_per_node) + overlap;
		const int y1 = input.width;
		ComputeLines(Crop(input, x0, y0, x1, y1), kernel, &output);
	}

	for (int i = 1; i < kNumNodes; ++i) {
		RgbMatrix<int> received(0, 0);
		MPI_RecvRgbMatrix(&received, i);
		Expand(received, &output);
	}

	return output;
}