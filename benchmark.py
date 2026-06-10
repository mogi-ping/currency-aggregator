import asyncio
import random
import time

import numpy as np

from sources import ALL_REQUESTS


def cpu_work():
    data = np.random.rand(2_000_000)
    return np.mean(data), np.std(data)


def run_sequential_baseline():
    start = time.perf_counter()

    for req in ALL_REQUESTS:
        if req["kind"] == "mock":
            time.sleep(random.uniform(0.1, 0.5))
        else:
            time.sleep(0.2)

        cpu_work()

    elapsed = time.perf_counter() - start

    print(f"Sequential time: {elapsed:.2f} sec")

    return elapsed


if __name__ == "__main__":
    run_sequential_baseline()