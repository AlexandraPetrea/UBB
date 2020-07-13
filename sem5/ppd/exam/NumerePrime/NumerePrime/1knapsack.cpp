#include"pch.h"
// NQueens.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <thread>
#include <vector>
#include <atomic>
#include <mutex>
/*
using namespace std;

mutex mtx;

vector<int> values{ 60,100,120,50 };
vector<int> weights{ 10,20,30,40 };

int const maxWeight = 50;
int bestValue = 0;

bool check(vector <int> v) {

	int s = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] == 1)
			s += weights[i];
	}
	if (s > maxWeight)
		return false;
	return true;
}

int maxValue(vector<int> v)
{
	int s = 0;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] == 1)
			s += values[i];
	}
	if (s < maxWeight)
		return bestValue;
	return s;
}



atomic <int> cnt;
vector<int> solution;
int N;

void back(int T, int m, int n) {

	if (T == 1) {
		for (int i = m; i < n; ++i) {
			vector <int> sol;
			for (int x = 0; x < N; ++x) {
				sol.push_back((i >> x) & 1);

			}

			if (check(sol) == true) {
				{
					mtx.lock();
					for (auto e : sol)
					{
						cout << e << " ";
					}

					cout << endl;
					mtx.unlock();
				}
				int valueOfThisSolution = maxValue(sol);
				if (bestValue < valueOfThisSolution)
				{
					bestValue = valueOfThisSolution;
					solution = sol;
				}
			}
		}

	}
	else {
		thread t([&]() {
			back(T / 2, m, n / 2);

		});

		back(T / 2, n / 2, n);

		t.join();
	}
}

int main() {
	N = weights.size();
	back(2, 0, 16);
	cout << "best value obtained:" << bestValue << endl;
	for (auto e : solution)
	{
		cout << e << " ";
	}
	int q;
	cin >> q;
}
*/