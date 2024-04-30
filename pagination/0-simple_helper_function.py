#!/usr/bin/env python3
""" Pagination project """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Helper function to return a tuple of size two containing
    a start index and an end index
     """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
