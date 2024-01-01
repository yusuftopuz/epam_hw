from pathlib import Path

import pytest

from homework1.task03 import EmptyFileError, find_maximum_and_minimum


def tests_func_returns_correct_values():
    """Testing that file exists gives true"""
    root_folder = Path(__file__).parents[2]
    path_to_file = (
        root_folder / "tests" / "homework1" / "supporting-files" / "some_file.txt"
    )
    assert find_maximum_and_minimum(path_to_file) == (1, 14)


def tests_func_works_if_file_exists():
    """Testing that file exists gives true"""
    root_folder = Path(__file__).parents[2]
    path_to_file = (
        root_folder / "tests" / "homework1" / "supporting-files" / "some_file.txt"
    )
    try:
        find_maximum_and_minimum(path_to_file)
    except FileNotFoundError:
        pytest.fail("Unexpected MyError ..")


def tests_raise_error_if_file_does_not_exist():
    """Testing that file exists gives true"""
    root_folder = Path(__file__).parents[2]
    path_to_file = (
        root_folder / "tests" / "homework1" / "supporting-files" / "does_not_exist.txt"
    )
    with pytest.raises(FileNotFoundError):
        find_maximum_and_minimum(path_to_file)


def test_file_is_empty():
    """Testing that file is empty return false"""
    root_folder = Path(__file__).parents[2]
    path_to_file = (
        root_folder / "tests" / "homework1" / "supporting-files" / "empty_file.txt"
    )
    with pytest.raises(EmptyFileError):
        find_maximum_and_minimum(path_to_file)
