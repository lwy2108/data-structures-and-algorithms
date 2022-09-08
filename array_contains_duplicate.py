"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


def array_contains_duplicate(nums):
  history = set()
  for num in nums:
    if num in history:
      return True
    history.add(num)
  return False


# test cases
case1 = [1,2,3,1]
case2 = [1,2,3,4]
case3 = [1,1,1,3,3,4,3,2,4,2]
print(case1, array_contains_duplicate(case1) is True)
print(case2, array_contains_duplicate(case2) is False)
print(case3, array_contains_duplicate(case3) is True)
