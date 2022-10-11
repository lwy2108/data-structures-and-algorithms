"""
Given an array A of size n, find the smallest int k that can zero out the array with at most m operations.

Each operation is a subtraction of k from any item i in A, where the item is tranformed into max(0, i - k)
"""

from math import ceil


def array_best_zeroer(n, m, A):
  k = ceil(sum(A) / m)
  while True:
    counter = [0] * n
    for i in range(n):
      x = A[i]
      counter[i] = ceil(x / k)
    if sum(counter) <= m:
      break
    k += 1
  return k


def array_best_zeroer(n, m, A):
  l, r = 1, max(A)
  res = r
  while l <= r:
    k = (l + r) // 2
    ops = 0
    for x in A:
      ops += ceil(x / k)
      if ops > m:
        l = k + 1
        break
    if ops <= m:
      res = min(res, k)
      r = k - 1
  return res


# test cases
n1, m1, A1 = 3, 9, [2, 5, 6]
n2, m2, A2 = 3, 4, [2, 3, 7]
print(n1, m1, A1, "Pass" if array_best_zeroer(n1, m1, A1) == 2 else "Fail")
print(n2, m2, A2, "Pass" if array_best_zeroer(n2, m2, A2) == 4 else "Fail")
