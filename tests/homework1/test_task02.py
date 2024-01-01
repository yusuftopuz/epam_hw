from homework1.task02 import check_fibonacci


def test_starts_with_zero_returns_true():
    """Testing that sequence starts with 0 gives True"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5])


def test_doesnt_start_with_zero_returns_false():
    """Testing that sequence doesn't start with 0 gives False"""
    assert not check_fibonacci([1, 1, 2, 3, 5])


def test_any_element_is_negative_returns_false():
    """Testing that any element is negative returns False"""
    assert not check_fibonacci([0, -1, -1, -2, -3])


def test_elements_of_fibonacci_sequence_mixed_returns_true():
    """If fib seq is mixed returns true"""
    assert check_fibonacci([2, 1, 1, 0, 3])


def test_when_sequence_is_too_short_returns_true():
    """If seq is too short returns true"""
    assert check_fibonacci([0, 1])
