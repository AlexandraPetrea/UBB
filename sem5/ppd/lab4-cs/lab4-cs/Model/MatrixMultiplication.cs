using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace lab4_cs.Model
{
    class MatrixMultiplication
    {
        private Matrix matrix1;
        private Matrix matrix2;
        private Matrix matrix3;
        private Matrix interMatrix;
        private Matrix resultMatrix;
        private Thread[] threadsF;
        private Thread[] threadsS;
        private static EventWaitHandle autoReset = new EventWaitHandle(false, EventResetMode.AutoReset);
        private static long threadCount = 0;
        private Mutex mutex = new Mutex();

        public MatrixMultiplication(Matrix matrix1, Matrix matrix2, Matrix matrix3)
        {
            this.matrix1 = matrix1;
            this.matrix2 = matrix2;
            this.matrix3 = matrix3;
            this.interMatrix = new Matrix(matrix1.GetNoRows(), matrix1.GetNoColumns());
            this.resultMatrix = new Matrix(matrix1.GetNoRows(), matrix1.GetNoColumns());
        }

        public Matrix GetResult() { return this.resultMatrix; }
        public Thread[] GetFirstLisThreads() { return this.threadsF; }
        public Thread[] GetSecondListThreads() { return this.threadsS; }
        public EventWaitHandle GetAutoResetEvent() { return autoReset; }
        public long GetThreadCount() { return threadCount; }

        private void InitThreads()
        {
            if (this.threadsF.Length.Equals(1))
            {
                this.threadsF[0] = new Thread(new ThreadStart(MulSeqF)) { Name = string.Format("FThread_" + 0) };
                this.threadsS[0] = new Thread(new ThreadStart(MulSeqS)) { Name = string.Format("SThread_" + 0) };
                this.threadsF[0].Start();
                this.threadsS[0].Start();
            }

            if (this.threadsF.Length.Equals(this.matrix1.GetNoRows()))
            {
                for (int i = 0; i < threadsF.Length; i++)
                {
                    int threadindex = i;
                    ThreadStart threadStartF = () => MulNF(threadindex);
                    ThreadStart threadStartS = () => MulNS(threadindex);
                    this.threadsF[i] = new Thread(threadStartF) { Name = string.Format("FThread_" + i) };
                    this.threadsS[i] = new Thread(threadStartS) { Name = string.Format("SThread_" + i) };
                    this.threadsF[i].Start();
                    this.threadsS[i].Start();
                }
            }
        }

        private void MulSeqF()
        {
            Debug.WriteLine(Thread.CurrentThread.Name + ":Start computing...");
            for (int i = 0; i < this.interMatrix.GetNoRows(); i++)
            {
                for (int j = 0; j < this.interMatrix.GetNoColumns(); j++)
                {
                    int col1 = j;
                    int sum = 0;
                    for (int k = 0; k < this.matrix2.GetNoRows(); k++)
                    {
                        sum = sum + this.matrix1.GetMatrixItem(i, k) * this.matrix2.GetMatrixItem(k, col1);
                    }
                    this.interMatrix.SetMatrixItem(i,
                                              col1,
                                              sum);
                }
            }
            Debug.WriteLine(Thread.CurrentThread.Name + ":Computed first and second matrix!");
            autoReset.Set();
        }

        private void MulSeqS()
        {
            Debug.WriteLine(Thread.CurrentThread.Name + ":Waiting !");
            autoReset.WaitOne();

            Debug.WriteLine(Thread.CurrentThread.Name + ":Computing The result !");
            for (int i = 0; i < this.resultMatrix.GetNoRows(); i++)
            {
                for (int j = 0; j < this.resultMatrix.GetNoColumns(); j++)
                {
                    int col1 = j;
                    int sum = 0;
                    for (int k = 0; k < this.matrix3.GetNoRows(); k++)
                    {
                        sum = sum + this.interMatrix.GetMatrixItem(i, k) * this.matrix3.GetMatrixItem(k, col1);
                    }
                    this.resultMatrix.SetMatrixItem(i,
                                                    col1,
                                                    sum);
                }
            }
            Debug.WriteLine(Thread.CurrentThread.Name + ":Done");
        }

        private void MulNF(int row)
        {
            Debug.WriteLine(Thread.CurrentThread.Name + ":Start computing...");
            for (int j = 0; j < this.interMatrix.GetNoColumns(); j++)
            {
                int col1 = j;
                int sum = 0;
                for (int k = 0; k < this.matrix2.GetNoRows(); k++)
                {
                    int col2 = k;
                    sum = sum + this.matrix1.GetMatrixItem(row, col2) * this.matrix2.GetMatrixItem(col2, col1);
                }
                this.interMatrix.SetMatrixItem(row,
                                          col1,
                                          sum);
            }
            Debug.WriteLine(Thread.CurrentThread.Name + ":Computed first and second matrix!");
            autoReset.Set();
        }

        private void MulNS(int row)
        {
            Debug.WriteLine(Thread.CurrentThread.Name + ":Waiting !");
            autoReset.WaitOne();

            Debug.WriteLine(Thread.CurrentThread.Name + ":Computing The result !");
            for (int j = 0; j < this.resultMatrix.GetNoColumns(); j++)
            {
                int col1 = j;
                int sum = 0;
                for (int k = 0; k < this.matrix3.GetNoRows(); k++)
                {
                    int col2 = k;
                    sum = sum + this.interMatrix.GetMatrixItem(row, col2) * this.matrix3.GetMatrixItem(col2, col1);
                }
                this.resultMatrix.SetMatrixItem(row,
                                          col1,
                                          sum);
            }
            threadCount--;
            Debug.WriteLine(Thread.CurrentThread.Name + ":Done");
        }

        public void SetNoThreads(int Code)
        {
            if (Code.Equals(1))
            {
                this.threadsF = new Thread[1];
                this.threadsS = new Thread[1];
            }
            if (Code.Equals(2))
            {
                this.threadsF = new Thread[this.matrix1.GetNoRows()];
                this.threadsS = new Thread[this.matrix1.GetNoRows()];
                threadCount = this.matrix1.GetNoRows();
            }
            Debug.WriteLine(this.threadsF.Length + " " + threadCount);
            InitThreads();
        }

    }
}