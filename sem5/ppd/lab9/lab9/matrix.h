#ifndef PDP_PROJECT_MATRIX_
#define PDP_PROJECT_MATRIX_

#include <cassert>
#include <vector>

template<typename T>
class Matrix {
public:
	Matrix<T>(int h, int w) : h_(h), w_(w), sum_(0),
		values_(h, std::vector<T>(w, 0)) {}
	Matrix<T>(const std::vector<std::vector<T>>& values) : h_(values.size()),
		w_(values[0].size()), sum_(0), values_(values) {
		for (int i = 0; i < h_; ++i) {
			for (int j = 0; j < w_; ++j) {
				sum_ += values_[i][j];
			}
		}
		if (!sum_) {
			sum_ = 1;
		}
	}
	Matrix<T>(const Matrix<T>& that) : h_(that.h_), w_(that.w_), sum_(that.sum_),
		values_(that.values_) {}

	int h() const {
		return h_;
	}

	int w() const {
		return w_;
	}

	int sum() const {
		return sum_;
	}

	T get(int i, int j) const {
		if (i < 0 || j < 0 || i >= h_ || j >= w_) {
			return 0;
		}
		return values_[i][j];
	}

	std::vector<T>& operator[](const int& i) {
		return values_[i];
	}

	const std::vector<T>& operator[](const int& i) const {
		return values_[i];
	}

	T convolute(const Matrix<T>& that, int x0, int y0) const {
		T value = 0;
		for (int i = 0; i < that.h_; ++i) {
			for (int j = 0; j < that.w_; ++j) {
				value += get(x0 + i, y0 + j) * that[i][j];
			}
		}
		return value / that.sum();
	}

	Matrix<T> crop(int x0, int y0, int x1, int y1) const {
		assert(x0 < x1);
		assert(y0 < y1);
		std::vector<std::vector<T>> rows(x1 - x0, std::vector<T>(y1 - y0, 0));
		for (int i = x0; i < x1; ++i) {
			for (int j = y0; j < y1; ++j) {
				rows[i - x0][j - y0] = get(i, j);
			}
		}
		return Matrix<T>(rows);
	}

	void expand(const Matrix<T>& matrix) {
		assert(w_ == matrix.w_);
		h_ += matrix.h_;
		for (auto& row : matrix.values_) {
			values_.push_back(row);
		}
		sum_ += matrix.sum_;
	}

private:
	int h_;
	int w_;
	T sum_;
	std::vector<std::vector<T>> values_;
};

#endif  // PDP_PROJECT_MATRIX_