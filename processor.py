import time
import numpy as np


def process_rate(data: dict) -> dict:
    """
    CPU-bound обработка одного полученного значения.
    Выполняется в отдельном процессе.
    """

    rate = float(data["rate"])

    samples = np.random.normal(
        loc=rate,
        scale=max(rate * 0.01, 0.0001),
        size=100_000
    )

    average_rate = float(np.mean(samples))
    std_dev = float(np.std(samples))

    return {
        "timestamp": time.time(),
        "currency_pair": data["pair"],
        "average_rate": average_rate,
        "std_dev": std_dev,
        "source": data["kind"],
        "cid": data["cid"]
    }