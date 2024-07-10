#!/usr/bin/env python3
"""Task 1.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(i: int, max_delay: int) -> List[float]:
    """Execute wait_random n time.
    """
    wait_time = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(i)))
    )
    return sorted(wait_time)
