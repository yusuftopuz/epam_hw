import pytest

from homework1.task04 import InputError, check_sum_of_four


def test_lists_are_not_empty():
    """Test none of the lists are empty and check_sum_of_four returns more than 0"""
    assert check_sum_of_four([1], [1], [0], [-2])


def test_if_any_list_is_empty_raise_error():
    """Test when any list is empty raises an error"""
    with pytest.raises(InputError):
        check_sum_of_four([1], [], [0], [4])


def test_lists_have_same_length():
    """Test all the lists involve same number of
    values and check_sum_of_four returns more than 0"""
    assert check_sum_of_four(
        [1, 3, 4, 1, 3, 4, 1, 3, 4, 1, 3, 4],
        [1, -3, 7, 1, 3, 4, 1, 3, 4, 1, 3, 4],
        [0, 2, -8, 1, 3, 4, 1, 3, 4, 1, 3, 4],
        [4, -5, -2, 1, 3, 4, 1, 3, 4, 1, 3, 4],
    )


def test_lists_do_not_have_same_length_raise_error():
    """Test when some lists do not have same length raises an error"""
    with pytest.raises(InputError):
        check_sum_of_four([1], [9, 8], [0, 1], [4, 9])
