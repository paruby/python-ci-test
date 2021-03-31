from src.code import example_code

from copy import deepcopy
from itertools import accumulate
from hypothesis import given
from hypothesis.strategies import lists, integers
import random


@given(input_list=lists(integers()), elem=integers())
def test_append_list(input_list, elem):
    _input_list = deepcopy(input_list)
    assert example_code.append_list(input_list, elem) == _input_list + [elem]


@given(positive_ints=lists(integers(min_value=0)), start=integers())
def test_merge_sort(positive_ints, start):
    _sorted = [start + i for i in accumulate(positive_ints)]
    unsorted = deepcopy(_sorted)
    random.shuffle(unsorted)
    assert example_code.merge_sort(unsorted=unsorted) == _sorted
