"""
Compute the nth Fibonacci number.
"""


def dp_memo_fib(n):  # T = O(2^n), S = O(n)
  if n <= 2:
    return 1
  return dp_memo_fib(n - 1) + dp_memo_fib(n - 2)


def dp_memo_fib(n, memo={}):  # T = O(n), S = O(n)
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  memo[n] = dp_memo_fib(n - 1) + dp_memo_fib(n - 2)
  return memo[n]


# test cases
n1 = 6
n2 = 7
n3 = 8
n4 = 50
print(n1, "Pass" if dp_memo_fib(n1) == 8 else "Fail")
print(n2, "Pass" if dp_memo_fib(n2) == 13 else "Fail")
print(n3, "Pass" if dp_memo_fib(n3) == 21 else "Fail")
print(n4, "Pass" if dp_memo_fib(n4) == 12586269025 else "Fail")
