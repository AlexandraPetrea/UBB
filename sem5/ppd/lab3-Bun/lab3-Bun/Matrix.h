#pragma once
#include <vector>

class Matrix
{
private:
	std::vector<std::vector<int>> content;
	int rows, cols;

public:
	Matrix();

	Matrix(int rows, int cols) : content(rows, std::vector<int>(cols))
	{
		this->rows = rows;
		this->cols = cols;

		int max = 90;
		int min = 10;

		for (int i = 0; i < this->rows; i++)
			for (int j = 0; j < this->cols; j++)
			{
				int random = rand() % 80 + 10;
				this->content[i][j] = random;
			}
	}

	std::string printMatrix();

	int index(int row, int col);
	void set(int row, int col, int value);
	int get(int row, int col);
	int getRowsNumber();
	int getColsNumber();

	~Matrix();
}; 
