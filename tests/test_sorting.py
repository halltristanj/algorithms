"""
test_sorting.py
~~~~~~~~~~~~~
Test all the algorithms algorithms
"""
import pytest
from random import sample

from algorithms.sorting import *


@pytest.fixture(scope="function")
def create_list():
    list_to_sort = sample(range(0, 100), 11)
    sorted_list = sorted(list_to_sort.copy())
    pytest.LOGGER.info(f"List to Sort: {list_to_sort}")
    pytest.LOGGER.info(f"Sorted List: {sorted_list}")
    return {"list": list_to_sort, "sorted_list": sorted_list}


def test_bubble_sort(create_list):
    """Test the bubble sort algorithm"""
    assert bubble_sort(create_list["list"]) == create_list["sorted_list"]


def test_insertion_sort(create_list):
    """Test the insertion sort algorithm"""
    assert insertion_sort(create_list["list"]) == create_list["sorted_list"]


def test_merge_sort(create_list):
    assert merge_sort(create_list["list"]) == create_list["sorted_list"]


def test_selection_sort(create_list):
    assert selection_sort(create_list["list"]) == create_list["sorted_list"]


if __name__ == "__main__":
    pytest.main(args=[__file__, "-vv"])
