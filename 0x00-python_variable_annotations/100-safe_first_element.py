#!/usr/bin/env python3
"""
Task 10: Duck typing - first element of a sequence
Augument code with correct duck-typed annotations
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
