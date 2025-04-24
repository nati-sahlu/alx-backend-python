#!/usr/bin/env python3
"""
Task 7: Complex types - string and int/float to tuple
Write typed-annotated function to_kv that takes str k and an int OR float v
Returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and its value to a tuple of the key and
    the square of its value.
    """
    return (k, v * v)
