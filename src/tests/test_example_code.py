from src.code import example_code


def test_append_list():
    assert example_code.append_list([1, 2, 3], 4) == [1, 2, 3, 4]
