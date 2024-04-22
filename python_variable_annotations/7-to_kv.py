#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a float n as argument and returns a tuple containing n and n squared."""
from typing import Union, Tuple, Callable, List, Iterator, Optional
def to_kv(k: Union[int, float]) -> Tuple[Union[int, float], float]:
    """Return tuple of int/float and float"""
    return (k, k ** 2)
