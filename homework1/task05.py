"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_array = 0
    for n in range(len(nums)):
        for i in range(1, k + 1):
            if i + n > len(nums):
                break
            else:
                if sum(nums[n : n + i]) > max_array:
                    max_array = sum(nums[n : n + i])
    return max_array


if __name__ == "__main__":
    nums = [1, 100, -4, 200, 5]
    print(find_maximal_subarray_sum(nums, 3))
