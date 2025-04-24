#!/usr/bin/env python3
"""
Task 11: More involved type annotations
Add type annotations to function safely_get_value
"""
from typing import Sequence, Union, Any, TypeVar, Mapping

R = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[R, None] = None) -> Union[Any, R]:
    """
    Retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
