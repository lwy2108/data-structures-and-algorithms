"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. There is exactly one solution.
"""


def array_two_sum(nums, target):
  map = {}
  for i, num in enumerate(nums):
    diff = target - num
    if diff in map:
      return [map[diff], i]
    else:
      map[num] = i


# test cases
nums1 = [2,7,11,15]
target1 = 9
nums2 = [3,2,4]
target2 = 6
nums3 = [3,3]
target3 = 6
print(nums1, target1, "Pass" if array_two_sum(nums1, target1) == [0, 1] else "Fail")
print(nums2, target2, "Pass" if array_two_sum(nums2, target2) == [1, 2] else "Fail")
print(nums3, target3, "Pass" if array_two_sum(nums3, target3) == [0, 1] else "Fail")
