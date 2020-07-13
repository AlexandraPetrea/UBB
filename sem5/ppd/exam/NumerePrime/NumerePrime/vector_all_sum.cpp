#include"pch.h"
#include <vector>
#include <chrono>
#include <future>
#include <thread>
#include <stdlib.h>
#include <stdio.h>
/*

using namespace std;

int vectorSum(vector<int>::const_iterator begin, vector<int>::const_iterator end,
	size_t nrThreads)
{
	if (nrThreads >= 2) {
		vector<int>::const_iterator mid = begin + (end - begin) / 2;
		future<int> fl(async([begin, mid, nrThreads]()->int
		{return vectorSum(begin, mid, nrThreads / 2); }));
		future<int> fr(async([end, mid, nrThreads]()->int
		{return vectorSum(mid, end, nrThreads - nrThreads / 2); }));
		return fl.get() + fr.get();
	}
	else {
		int s = 0;
		for (vector<int>::const_iterator it = begin; it != end; ++it) s += *it;
		return s;
	}
}

void generate(vector<int>& v, size_t n)
{
	v.clear();
	v.reserve(n);
	for (size_t i = 0; i < n; ++i) {
		v.push_back(rand());
	}
}

void printVector(vector<int> const& v)
{
	printf("Vector =");
	for (int val : v) printf(" %d", val);
	printf("\n");
}

bool checkSum(vector<int> const& a, int s)
{
	int tmp = 0;
	for (int v : a) {
		tmp += v;
	}
	return (s == tmp);
}

int main(int argc, char** argv)
{
	unsigned n = 0;
	unsigned nrThreads = 0;
	if (argc != 3 || 1 != sscanf_s(argv[1], "%u", &n) || 1 != sscanf_s(argv[2], "%u", &nrThreads)) {
		fprintf(stderr, "usage: vectorSum <n> <nrThreads>\n");
		return 1;
	}

	vector<int> a;
	int s;
	generate(a, n);

	chrono::high_resolution_clock::time_point const beginTime = chrono::high_resolution_clock::now();
	s = vectorSum(a.begin(), a.end(), nrThreads);
	chrono::high_resolution_clock::time_point const endTime = chrono::high_resolution_clock::now();

	printf("Result %s, time=%ldms\n", (checkSum(a, s) ? "ok" : "FAIL"),
		(chrono::duration_cast<chrono::milliseconds>(endTime - beginTime)).count());
}
*/