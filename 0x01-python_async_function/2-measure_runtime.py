#!/usr/bin/env python3
"""Creates a measure_time function with integers n
and max_delay as arguments that measures the total
execution time for wait_n(n, max_delay),
and returns total_time / n"""

import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for a function"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
