"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


class InputError(Exception):
    """Raises error lists are not in same length"""

    pass


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> None:
    """Calculates sum of four lists are zero"""
    counter = 0
    sum_two_elem = dict()
    if len(a) == len(b) == len(c) == len(d) >= 1:
        for i in a:
            for j in b:
                if i + j in sum_two_elem:
                    sum_two_elem[i + j] += 1
                else:
                    sum_two_elem[i + j] = 1

        for k in c:
            for l in d:
                if -(k + l) in sum_two_elem:
                    counter += sum_two_elem[-(k + l)]
        return counter
    else:
        raise InputError(
            "Lists should contain the same number "
            f"of values and should not be empty, given:\n{a, b, c, d}"
        )
