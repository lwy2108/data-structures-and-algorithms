"""
Given an array A of size n, find the smallest int k that can zero out the array with at most m operations.

Each operation is a subtraction of k from any item i in A, where the item is tranformed into max(0, i - k)
"""

from math import ceil


def array_best_zeroer(n, m, A):
  k = 1
  while True:
    counter = [0] * n
    for i in range(n):
      x = A[i]
      counter[i] = ceil(x / k)
    if sum(counter) <= m:
      break
    k += 1
  return k


# test cases
n = 3
m = 9
A = [2, 5, 6]
print(n, m, A, "Pass" if array_best_zeroer(n, m, A) == 2 else "Fail")
