#!/usr/bin/env python3
"""Type-annotated function sum_list that takes a list input_list of floats as argument and returns their sum as a float."""
from typing import List
def sum_list(input_list: List[float]) -> float:
    """Return sum of floats in list"""
    return sum(input_list)