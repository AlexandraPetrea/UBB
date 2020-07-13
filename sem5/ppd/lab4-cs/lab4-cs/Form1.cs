using lab4_cs.Model;
using System;
using System.Diagnostics;
using System.Threading;

namespace lab4_cs
{
    public partial class Form1 : Form
    {
        private Matrix matrix1;
        private Matrix matrix2;
        private Matrix matrix3;
        private MatrixMultiplication matMul;

        public Form1()
        {
            InitializeComponent();
            ThreadRButton.Checked = true;
            Init();
        }

        private void GenerateBtn_Click(object sender, EventArgs e)
        {
            Init();
        }

        private void InitMatrix()
        {
            Random random = new Random();
            for (int i = 0; i < matrix1.GetNoRows(); i++)
                for (int j = 0; j < matrix1.GetNoColumns(); j++)
                    matrix1.SetMatrixItem(i, j, random.Next(1, 3));

            for (int i = 0; i < matrix2.GetNoRows(); i++)
                for (int j = 0; j < matrix2.GetNoColumns(); j++)
                    matrix2.SetMatrixItem(i, j, random.Next(1, 3));

            for (int i = 0; i < matrix2.GetNoRows(); i++)
                for (int j = 0; j < matrix2.GetNoColumns(); j++)
                    matrix3.SetMatrixItem(i, j, random.Next(1, 3));
        }

        private void DisplayMatrix(Matrix matrix, Panel MatrixPanel)
        {
            Button[,] labels = new Button[matrix.GetNoRows(), matrix.GetNoColumns()];
            MatrixPanel.Controls.Clear();
            for (int i = 0; i < matrix.GetNoRows(); i++)
            {
                for (int j = 0; j < matrix.GetNoColumns(); j++)
                {
                    labels[i, j] = new Button()
                    {
                        Width = 40,
                        Height = 20,
                        Text = matrix.GetMatrixItem(i, j).ToString(),
                        Location = new Point(j * 37 + 10, i * 17 + 10),
                        Parent = MatrixPanel,
                    };
                }
            }
        }

        private void Init()
        {
            ResultPanel.Controls.Clear();
            TimeTextBox.Clear();
            Random rnd = new Random();
            int size = rnd.Next(1, 5);
            matrix1 = new Matrix(size, size);
            matrix2 = new Matrix(size, size);
            matrix3 = new Matrix(size, size);
            InitMatrix();
            DisplayMatrix(matrix1, MatPanel1);
            DisplayMatrix(matrix2, MatPanel2);
            DisplayMatrix(matrix3, MatPanel3);
        }

        private void CheckThreads()
        {
            if (ThreadRButton.Checked.Equals(true))
                matMul.SetNoThreads(1);
            if (NThreadRButton.Checked.Equals(true))
                matMul.SetNoThreads(2);
        }

        private void MulBtn_Click(object sender, EventArgs e)
        {
            Stopwatch stopwatch = new Stopwatch();
            matMul = new MatrixMultiplication(matrix1, matrix2, matrix3);
            stopwatch.Start();
            CheckThreads();
            foreach (Thread th in matMul.GetFirstLisThreads())
                th.Join();
            foreach (Thread th in matMul.GetSecondListThreads())
                th.Join();

            CloseThreads();
            stopwatch.Stop();
            Matrix matrix = matMul.GetResult();
            DisplayMatrix(matrix, ResultPanel);
            TimeTextBox.Text = stopwatch.Elapsed.ToString();
        }

        private void CloseThreads()
        {
            foreach (Thread th in matMul.GetFirstLisThreads())
                th.Abort();
            foreach (Thread th in matMul.GetSecondListThreads())
                th.Abort();
        }

        private void DisplayBtn_Click(object sender, EventArgs e)
        {

        }
    }
}