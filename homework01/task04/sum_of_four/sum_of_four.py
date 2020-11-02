"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sum_of_two = {}
    for i in a:
        for j in b:
            if i + j not in sum_of_two:
                sum_of_two[i + j] = 1
            else:
                sum_of_two[i + j] += 1
    tuple_count = 0
    for i in c:
        for j in d:
            if -(i + j) in sum_of_two:
                tuple_count += sum_of_two[-(i + j)]
    return tuple_count


a = [0, 2]
b = [1, 2]
c = [3, -2]
d = [4, 2]
n = check_sum_of_four(a, b, c, d)
print(n)
