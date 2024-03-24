import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import timeit

import matplotlib.pyplot as plt


def split_indexes(a, n):
    k, m = divmod(len(a), n)
    return ((i*k+min(i, m), (i+1)*k+min(i+1, m)) for i in range(n))


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_interval(f, a, left, right, step):
    acc = 0
    for i in range(left, right):
        acc += f(a + i * step) * step
    return acc


def integrate_sync(f, a, b, *, n_jobs=1, n_iter=10000000):
    accs = []
    step = (b - a) / n_iter
    intervals = list(split_indexes(range(n_iter), n_jobs))
    for left, right in intervals:
        acc = integrate_interval(f, a, left, right, step)
        accs.append(acc)
    return sum(accs)


def integrate_thread(f, a, b, *, n_jobs=1, n_iter=10000000):
    accs = []
    step = (b - a) / n_iter
    intervals = list(split_indexes(range(n_iter), n_jobs))
    with ThreadPoolExecutor(max_workers=n_jobs) as ex:
        futures = []
        for left, right in intervals:
            future = ex.submit(integrate_interval, f, a, left, right, step)
            futures.append(future)
        for future in futures:
            accs.append(future.result())
    return sum(accs)


def integrate_processes(f, a, b, *, n_jobs=1, n_iter=10000000):
    accs = []
    step = (b - a) / n_iter
    intervals = list(split_indexes(range(n_iter), n_jobs))
    with ProcessPoolExecutor(max_workers=n_jobs) as ex:
        futures = []
        for left, right in intervals:
            future = ex.submit(integrate_interval, f, a, left, right, step)
            futures.append(future)
        for future in futures:
            accs.append(future.result())
    return sum(accs)


def linear(x):
    return x


print(integrate(linear, 0, 2, n_iter=100))
print(integrate_sync(linear, 0, 2, n_jobs=10, n_iter=100))
print(integrate_thread(linear, 0, 2, n_jobs=10, n_iter=100))
print(integrate_processes(linear, 0, 2, n_jobs=10, n_iter=100))


def calculate_time(func, f, a, b, n_jobs):
    start_time = timeit.default_timer()
    func(f, a, b, n_jobs=n_jobs)
    end_time = timeit.default_timer()
    return end_time - start_time


syncs = []
threads = []
processes = []
num_jobs = list(range(1, 25))
for i in num_jobs:
    print(f"Number of Jobs: {i}")
    time_sync = calculate_time(
        integrate_sync, math.cos, 0, math.pi / 2, n_jobs=i)
    print(f"Time taken by Sync: {time_sync} seconds")
    syncs.append(time_sync)

    time_thread = calculate_time(
        integrate_thread, math.cos, 0, math.pi / 2, n_jobs=i)
    print(f"Time taken by Threads: {time_thread} seconds")
    threads.append(time_thread)

    time_processes = calculate_time(
        integrate_processes, math.cos, 0, math.pi / 2, n_jobs=i)
    print(f"Time taken by Processes: {time_processes} seconds")
    processes.append(time_processes)
    print("-------------------------")


plt.plot(num_jobs, syncs, label='Sync')
plt.plot(num_jobs, threads, label='Threads')
plt.plot(num_jobs, processes, label='Processes')

plt.xlabel('Number of Jobs')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Execution Time')
plt.legend()

plt.show()
