import threading
import multiprocessing
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time} "
              "seconds")
        return result
    return wrapper


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@timer
def run_sync(fibonacci_num, n_sync):
    for _ in range(n_sync):
        fibonacci(fibonacci_num)


@timer
def run_threads(fibonacci_num, n_threads):
    threads = []
    for _ in range(n_threads):
        thread = threading.Thread(target=fibonacci, args=(fibonacci_num,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


@timer
def run_processes(fibonacci_num, n_processes):
    processes = []
    for _ in range(n_processes):
        process = multiprocessing.Process(
            target=fibonacci, args=(fibonacci_num,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


def main():
    number = 35
    run_n_times = 10
    run_threads(number, run_n_times)
    run_processes(number, run_n_times)
    run_sync(number, run_n_times)


if __name__ == "__main__":
    main()
