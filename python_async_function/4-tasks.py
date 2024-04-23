#!/usr/bin/env python3
""" Basic asyncio task """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task_wait_random n times"""

    queue, array = [], []

    for _ in range(n):
        queue.append(task_wait_random(max_delay))

    for q in asyncio.as_completed(queue):
        result = await q
        array.append(result)

    return array
