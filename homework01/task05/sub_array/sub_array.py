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
    if len(nums) == 0:
        return 0
    if k <= 0:
        raise ValueError("k must be greater than 0.")
    max_sum = nums[0]
    for n in range(1, min(k, len(nums)) + 1):
        for i in range(len(nums) - n + 1):
            current_sum = sum(nums[i : i + n])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
