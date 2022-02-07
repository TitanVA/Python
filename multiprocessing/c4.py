import concurrent.futures
import multiprocessing
import time


def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done Sleeping... {seconds}"


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [1, 4, 3, 5, 2]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     results = [executor.submit(do_something, sec) for sec in secs]
    #
    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=(1.5,))
    #     p.start()
    #     processes.append(p)
    # for process in processes:
    #     process.join()

    finish = time.perf_counter()
    print(f"Finishing in {round(finish - start, 2)} second(s)")
