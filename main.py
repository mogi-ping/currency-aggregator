import asyncio
import logging

from aggregator import CurrencyAggregator
from storage import init_db


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(processName)s | %(threadName)s | %(message)s"
)


async def main():
    init_db()

    agg = CurrencyAggregator()

    logging.info("Program started")

    await agg.collect()

    await agg.process_data()

    await agg.store_data()

    logging.info("Program finished")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped by user")