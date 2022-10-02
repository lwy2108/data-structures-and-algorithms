"""
Find the total number of ways to travel through a grid of size n x m.
"""


def dp_memo_grid_traveler(m, n):  # T = O(2^(m+n)), S = O(m+n)
  if m == 0 or n == 0:
    return 0
  if m == 1 or n == 1:
    return 1
  return dp_memo_grid_traveler(m - 1, n, memo) + dp_memo_grid_traveler(m, n - 1, memo)


def dp_memo_grid_traveler(m, n, memo={}):  # T = O(m*n), S = O(m+n)
  if (m, n) in memo:
    return memo[(m, n)]
  if m == 0 or n == 0:
    return 0
  if m == 1 or n == 1:
    return 1
  memo[(m, n)] = dp_memo_grid_traveler(m - 1, n, memo) + dp_memo_grid_traveler(m, n - 1, memo)
  return memo[(m, n)]


# test cases
m1 = 1
n1 = 1
m2 = 2
n2 = 3
m3 = 3
n3 = 3
m4 = 18
n4 = 18
print(m1, n1, "Pass" if dp_memo_grid_traveler(m1, n1) == 1 else "Fail")
print(m2, n2, "Pass" if dp_memo_grid_traveler(m2, n2) == 3 else "Fail")
print(m3, n3, "Pass" if dp_memo_grid_traveler(m3, n3) == 6 else "Fail")
print(m4, n4, "Pass" if dp_memo_grid_traveler(m4, n4) == 2333606220 else "Fail")
