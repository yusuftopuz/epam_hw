"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import List


def check_fibonacci(data: List[int], n=0) -> bool:
    data.sort()
    if data == [0, 1]:
        return True
    if data[0] != 0:
        return False
    for x in range(n, len(data) - 2):
        if data[x] + data[x + 1] == data[x + 2]:
            if x + 2 == len(data) - 1:
                return True
            check_fibonacci(data, n + 1)
        else:
            return False


if __name__ == "__main__":
    f = [0, 1, 1, 1]

    print(check_fibonacci(f))
