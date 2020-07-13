using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab4_cs.Model
{
    class Matrix
    {
        private int NoColumns;
        private int NoRows;
        private int[,] matrix;

        public Matrix(int NoRows, int NoColumns)
        {
            this.NoColumns = NoColumns;
            this.NoRows = NoRows;
            this.matrix = new int[this.NoRows, this.NoColumns];
        }

        public int GetNoColumns() { return this.NoColumns; }
        public int GetNoRows() { return this.NoRows; }
        public int GetMatrixItem(int row, int column) { return this.matrix[row, column]; }
        public void SetMatrixItem(int row, int column, int val) { this.matrix[row, column] = val; }
        public void SetNoColumns(int NoColumn) { this.NoColumns = NoColumn; }
        public void SetNoRows(int NoRow) { this.NoRows = NoRow; }

        public override string ToString()
        {
            string str = "";

            for (int i = 0; i < NoRows; i++)
            {
                for (int j = 0; j < NoColumns; j++)
                    str += matrix[i, j] + " ";
                str += "\n";
            }

            return str;
        }
    }
}