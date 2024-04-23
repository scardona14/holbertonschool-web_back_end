#!/usr/bin/env python3
"""
Measure the runtime
"""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def runtime(n: int, max_delay: int) -> float:
    """
    Measure the runtime
    """
    start = time.time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n
