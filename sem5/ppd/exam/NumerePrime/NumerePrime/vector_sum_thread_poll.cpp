#include"pch.h"
#include <stdio.h>
#include <stdint.h>
#include <atomic>
#include <thread>
#include <vector>
#include <mutex>
#include <algorithm>
#include <functional>
#include <condition_variable>
#include <list>

class ThreadPool {
public:
	explicit ThreadPool(size_t nrThreads)
		:m_end(false),
		m_liveThreads(nrThreads)
	{
		m_threads.reserve(nrThreads);
		for (size_t i = 0; i < nrThreads; ++i) {
			m_threads.emplace_back([this]() {this->run(); });
		}
	}

	~ThreadPool() {
		close();
		for (std::thread& t : m_threads) {
			t.join();
		}
	}

	void close() {
		std::unique_lock<std::mutex> lck(m_mutex);
		m_end = true;
		m_cond.notify_all();
		while (m_liveThreads > 0) {
			m_condEnd.wait(lck);
		}
	}

	void enqueue(std::function<void()> func) {
		std::unique_lock<std::mutex> lck(m_mutex);
		m_queue.push_back(std::move(func));
		m_cond.notify_one();
	}

	//    template<typename Func, typename... Args>
	//    void enqueue(Func func, Args&&... args) {
	//        std::function<void()> f = [=](){func(args...);};
	//        enqueue(std::move(f));
	//    }
private:
	void run() {
		while (true) {
			std::function<void()> toExec;
			{
				std::unique_lock<std::mutex> lck(m_mutex);
				while (m_queue.empty() && !m_end) {
					m_cond.wait(lck);
				}
				if (m_queue.empty()) {
					--m_liveThreads;
					if (0 == m_liveThreads) {
						m_condEnd.notify_all();
					}
					return;
				}
				toExec = std::move(m_queue.front());
				m_queue.pop_front();
			}
			toExec();
		}
	}

	std::mutex m_mutex;
	std::condition_variable m_cond;
	std::condition_variable m_condEnd;
	std::list<std::function<void()> > m_queue;
	bool m_end;
	size_t m_liveThreads;
	std::vector<std::thread> m_threads;
};

std::unique_ptr<int[]> a, b;

void func(size_t start, size_t len, size_t iterations)
{
	for (size_t k = 0; k < iterations; ++k) {
		for (uint64_t i = 0; i < len; ++i) {
			a[start + i] = b[start + i] * b[start + i] * int(k);
		}
	}
}

int main(int argc, char** argv)
{
	long long nrTasks;
	long long lenPerThread;
	long long iterations;
	long long nrThreads;
	if (argc != 5 || 1 != sscanf(argv[1], "%lld", &nrTasks)
		|| 1 != sscanf(argv[2], "%lld", &lenPerThread)
		|| 1 != sscanf(argv[3], "%lld", &iterations)
		|| 1 != sscanf(argv[4], "%lld", &nrThreads)) {
		fprintf(stderr, "Usage: vector_sum_multithread nrThreads lenPerThread iterations maxThreads\n");
		return 1;
	}

	long long totalSize = nrTasks * lenPerThread;
	a.reset(new int[totalSize]);
	b.reset(new int[totalSize]);

	ThreadPool pool(nrThreads);

	for (unsigned i = 0; i < nrTasks; ++i) {
		pool.enqueue([i, lenPerThread, iterations]() {func(lenPerThread*i, lenPerThread, iterations); });
	}
	pool.close();
}
