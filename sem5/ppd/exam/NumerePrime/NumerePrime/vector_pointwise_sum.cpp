#include"pch.h"
#include <vector>
#include <chrono>
#include <future>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

void partSumChunks(vector<int> const& a, vector<int> const& b, vector<int>& c,
	size_t nrThreads, size_t t)
{
	size_t const n = a.size();
	size_t const begin = (t*n) / nrThreads;
	size_t const end = ((t + 1)*n) / nrThreads;
	for (size_t i = begin; i < end; ++i) {
		c[i] = a[i] + b[i];
	}
}

void partSumInterlaced(vector<int> const& a, vector<int> const& b, vector<int>& c,
	size_t nrThreads, size_t t)
{
	size_t const n = a.size();
	for (size_t i = t; i < n; i += nrThreads) {
		c[i] = a[i] + b[i];
	}
}

void vectorSum(vector<int> const& a, vector<int> const& b, vector<int>& c,
	unsigned nrThreads)
{
	size_t const n = a.size();
	vector<future<void> > futures;
	futures.reserve(nrThreads);
	for (size_t i = 0; i < nrThreads; ++i) {
		futures.push_back(async([&a, &b, &c, i, nrThreads]()->void {
			partSumChunks(a, b, c, nrThreads, i);
		}));
	}
	for (auto& f : futures) {
		f.get();
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

bool checkSum(vector<int> const& a, vector<int> const& b, vector<int> const& s)
{
	if (a.size() != s.size() || b.size() != s.size()) return false;
	for (size_t i = 0; i < s.size(); ++i) {
		if (s[i] != a[i] + b[i]) return false;
	}
	return true;
}

int main(int argc, char** argv)
{
	unsigned n = 0;
	unsigned nrThreads = 0;
	if (argc != 3 || 1 != sscanf_s(argv[1], "%u", &n) || 1 != sscanf_s(argv[2], "%u", &nrThreads)) {
		fprintf(stderr, "usage: vectorSum <n> <nrThreads>\n");
		return 1;
	}

	vector<int> a, b, c;
	generate(a, n);
	generate(b, n);

	c.resize(n);
	chrono::high_resolution_clock::time_point const beginTime = chrono::high_resolution_clock::now();
	vectorSum(a, b, c, nrThreads);
	printf("Result %s",c);
	chrono::high_resolution_clock::time_point const endTime = chrono::high_resolution_clock::now();

	printf("Result %s, time=%ldms\n", (checkSum(a, b, c) ? "ok" : "FAIL"),
		(chrono::duration_cast<chrono::milliseconds>(endTime - beginTime)).count());
}
