#ifndef PDP_PROJECT_KERNELS_
#define PDP_PROJECT_KERNELS_

#include <string>
#include <vector>

#include "matrix.h"

class Kernels {
public:
	static Matrix<int> kernel(int i) {
		return Matrix<int>(kernels[i]);
	}

	static std::string name(int i) {
		return names[i];
	}

	static int num_kernels() {
		return kernels.size();
	}

private:
	static const std::vector<std::vector<std::vector<int>>> kernels;
	static const std::vector<std::string> names;
};

const std::vector<std::vector<std::vector<int>>> Kernels::kernels = {
	// identity
	{ { 0, 0, 0},
	  { 0, 1, 0},
	  { 0, 0, 0}
	},

	// boxed blur
	{ { 1, 1, 1},
	  { 1, 1, 1},
	  { 1, 1, 1}
	},

	// sharpening
	{ {0, -1, 0},
	  { -1, 5, -1},
	  {0, -1, 0}
	},

	// gaussian blur 5x5
	{ {1, 4, 6, 4, 1},
	  {4, 16, 24, 16, 4},
	  {6, 24, 36, 24, 6},
	  {4, 16, 24, 16, 4},
	  {1, 4, 6, 4, 1}
	},

	// edge detection
	{ { -1, -1, -1},
	  { -1, 8, -1},
	  { -1, -1, -1}
	},
};

const std::vector<std::string> Kernels::names = {
  "identity",
  "boxed blur",
  "sharpening",
  "gaussian blur 5x5",
  "edge detection",
};

#endif  // PDP_PROJECT_KERNELS_