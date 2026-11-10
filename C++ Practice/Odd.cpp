
#include <iostream>
#include <chrono>
#include <cmath>
#include <thread>
#include <vector>
#include <iomanip>

using namespace std;
using namespace chrono;

double calculate(long long n) {
    double sum = 0.0;

    for (long long i = 1; i <= n; ++i) {
        sum += sqrt(static_cast<double>(i));
    }

    return sum;
}

int main() {
    unsigned int cores = thread::hardware_concurrency();
    if (cores == 0) cores = 1;

    const long long iterations = 20000000LL;

    cout << "=== C++ PC CPU BENCHMARK ===\n";
    cout << "Logical CPU cores: " << cores << "\n";

    auto start = steady_clock::now();
    volatile double singleResult = calculate(iterations);
    auto end = steady_clock::now();

    double singleTime = duration<double>(end - start).count();
    cout << fixed << setprecision(3);
    cout << "Single-core time: " << singleTime << " seconds\n";

    vector<thread> workers;
    vector<double> results(cores);

    start = steady_clock::now();

    for (unsigned int i = 0; i < cores; ++i) {
        workers.emplace_back([&, i]() {
            results[i] = calculate(iterations);
        });
    }

    for (auto& worker : workers)
        worker.join();

    end = steady_clock::now();

    double multiTime = duration<double>(end - start).count();
    cout << "Multi-core time: " << multiTime << " seconds\n";
    cout << "Parallel speedup: "
         << singleTime / multiTime << "x\n";

    cout << "Checksum: " << singleResult + results[0] << "\n";
    cout << "Benchmark complete!\n";

    return 0;
}
