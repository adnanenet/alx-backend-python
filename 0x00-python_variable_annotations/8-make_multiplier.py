#!/usr/bin/env python3
"""Task 8.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier.
    """
    return lambda x: x * multiplier
