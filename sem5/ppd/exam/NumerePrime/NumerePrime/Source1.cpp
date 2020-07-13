#include<pch.h>
#include <iostream>
#include <vector>
#include <time.h>
#include <chrono>
#include <stdint.h>

using namespace std;

void generate(vector<int>& v, size_t n)
{
	v.reserve(n);
	for (size_t i = 0; i < n; ++i) {
		// v.push_back(rand());
		v.push_back((i * 101011) % 123456);
	}
}

inline bool checkSum(const vector <int> &v, int sum) {
	int _sum = 0;
	for (auto it : v) {
		_sum += it;
	}
	return _sum == sum;
}

void slaveSum(int me) {
	int n;
	MPI_Status status;
	MPI_Recv(&n, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);

	vector <int> chunk;
	chunk.resize(n);

	MPI_Recv(chunk.data(), n, MPI_INT, 0, 2, MPI_COMM_WORLD, &status);

	int sum = 0;
	for (auto it : chunk) {
		sum += it;
	}
	cout << "slaveSum::bSend " << me << ' ' << n << '\n';

	MPI_Ssend(&sum, 1, MPI_INT, 0, 3, MPI_COMM_WORLD);
}

int vectorSum(const vector <int> &v, int nrProcs) {
	int n = v.size();
	for (int i = 1; i < nrProcs; ++i) {
		int st = (i * n) / nrProcs;
		int fn = ((i + 1) * n) / nrProcs;
		int nElem = fn - st;
		cout << "vectorSum::bSend " << nElem << ' ' << st << ' ' << fn << '\n';
		MPI_Ssend(&nElem, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
		cout << "vectorSum::bSend 2\n";
		MPI_Ssend(v.data() + st, nElem, MPI_INT, i, 2, MPI_COMM_WORLD);
		cout << "vectorSum::bSend done\n";
	}
	int sum = 0;
	for (int i = 0; i < n / nrProcs; ++i) {
		sum += v[i];
	}
	for (int i = 1; i < nrProcs; ++i) {
		int current_sum;
		MPI_Status status;
		MPI_Recv(&current_sum, 1, MPI_INT, i, 3, MPI_COMM_WORLD, &status);
		sum += current_sum;
	}
	return sum;
}


int main(int argc, char** argv)
{
	MPI_Init(0, 0);
	int me;
	int nrProcs;
	MPI_Comm_size(MPI_COMM_WORLD, &nrProcs);
	MPI_Comm_rank(MPI_COMM_WORLD, &me);

	unsigned n;
	vector<int> v;
	if (argc != 2 || 1 != sscanf(argv[1], "%u", &n)) {
		fprintf(stderr, "usage: sum-mpi <n>\n");
		return 1;
	}


	if (me == 0) {
		generate(v, n);
		fprintf(stderr, "generated\n");
		chrono::high_resolution_clock::time_point const beginTime = chrono::high_resolution_clock::now();

		int sum = vectorSum(v, nrProcs);
		chrono::high_resolution_clock::time_point const endTime = chrono::high_resolution_clock::now();

		printf("Result %s, time=%ldms\n", (checkSum(v, sum) ? "ok" : "FAIL"),
			(chrono::duration_cast<chrono::milliseconds>(endTime - beginTime)).count());
	}
	else {
		// slave
		chrono::high_resolution_clock::time_point const beginTime = chrono::high_resolution_clock::now();
		slaveSum(me);
		chrono::high_resolution_clock::time_point const endTime = chrono::high_resolution_clock::now();

		printf("(slave %d): time=%ldms\n", me,
			(chrono::duration_cast<chrono::milliseconds>(endTime - beginTime)).count());
	}
	MPI_Finalize();
}