import asyncio
import logging
import random

import aiohttp

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue

from sources import ALL_REQUESTS
from processor import process_rate
from storage import save_rate


class CurrencyAggregator:

    def __init__(self):
        self.raw_queue = asyncio.Queue()
        self.processed_queue = Queue()

    async def _fetch(self, session, req):

        if req["kind"] == "mock":
            await asyncio.sleep(random.uniform(0.1, 0.5))

            result = {
                "pair": req["pair"],
                "base": req["base"],
                "target": req["target"],
                "rate": random.uniform(0.5, 150.0),
                "kind": "mock",
                "cid": req["cid"]
            }

            logging.info(f"Collected {req['cid']}")

            return result

        try:
            async with session.get(req["url"]) as resp:

                if resp.status != 200:
                    logging.warning(f"Request failed {req['cid']}")
                    return None

                data = await resp.json()

                if req["kind"] == "frankfurter":
                    rate = list(data["rates"].values())[0]

                elif req["kind"] == "binance":
                    rate = float(data["price"])

                else:
                    return None

                result = {
                    "pair": req["pair"],
                    "base": req["base"],
                    "target": req["target"],
                    "rate": rate,
                    "kind": req["kind"],
                    "cid": req["cid"]
                }

                logging.info(f"Collected {req['cid']}")

                return result

        except Exception:
            logging.warning(f"Error {req['cid']}")
            return None

    async def collect(self):

        timeout = aiohttp.ClientTimeout(total=5)

        async with aiohttp.ClientSession(timeout=timeout) as session:

            tasks = [
                self._fetch(session, req)
                for req in ALL_REQUESTS
            ]

            results = await asyncio.gather(*tasks)

            for item in results:
                if item is not None:
                    await self.raw_queue.put(item)

            await self.raw_queue.put(None)

    async def process_data(self):

        loop = asyncio.get_running_loop()

        with ProcessPoolExecutor() as pool:

            while True:

                item = await self.raw_queue.get()

                if item is None:
                    self.processed_queue.put(None)
                    break

                result = await loop.run_in_executor(
                    pool,
                    process_rate,
                    item
                )

                logging.info(f"Processed {item['cid']}")

                self.processed_queue.put(result)

    async def store_data(self):

        loop = asyncio.get_running_loop()

        with ThreadPoolExecutor() as pool:

            while True:

                item = self.processed_queue.get()

                if item is None:
                    break

                await loop.run_in_executor(
                    pool,
                    save_rate,
                    item
                )

                logging.info(f"Saved {item['cid']}")