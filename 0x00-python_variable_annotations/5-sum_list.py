#!/usr/bin/env python3
"""
Task 5: Complex types - list of floats
Write type-annotated function sum_list, takes input_list of floats
as arguments
Returns their sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floating-point numbers.
    """
    return sum(input_list)
