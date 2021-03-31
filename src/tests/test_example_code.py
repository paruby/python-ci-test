from src.code import example_code
from copy import deepcopy
from hypothesis import given
from hypothesis.strategies import lists, integers


@given(input_list=lists(integers()), elem=integers())
def test_append_list(input_list, elem):
    _input_list = deepcopy(input_list)
    assert example_code.append_list(input_list, elem) == _input_list + [elem]
