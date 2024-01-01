"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return (1, 5)

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:
a = []
with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
import os
from pathlib import Path
from typing import Tuple, Union


class EmptyFileError(Exception):
    pass


def find_maximum_and_minimum(file_name: Union[str, Path]) -> Tuple[int, int]:
    check_file = os.path.isfile(file_name)
    if not check_file:
        raise FileNotFoundError("File does not exist")

    with open(file_name) as f:
        data = f.read().split("\n")
    if data == [""]:
        raise EmptyFileError("There were not any information in the file")
    # shorter: data = [int(value) for value in f.read().split("\n")]
    data = [int(value) for value in data]
    minimum = maximum = data[0]
    for value in data:
        if value > maximum:
            maximum = value

        elif value < minimum:
            minimum = value

    return minimum, maximum
