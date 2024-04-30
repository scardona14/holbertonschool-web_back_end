#!/usr/bin/env python3
""" Pagination project """
from typing import List, Tuple
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Helper function to return a tuple of size two containing a start
    index and an end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """ Server class to paginate a database of popular baby names """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Constructor of the Server class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Loads dataset from CSV """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get the dataset with pagination """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()

        if self.__dataset is None:
            return []

        idx_range = index_range(page, page_size)
        data = self.__dataset[idx_range[0]:idx_range[1]]
        return data
