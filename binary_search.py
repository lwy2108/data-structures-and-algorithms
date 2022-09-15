"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.

If target exists, then return its index. Otherwise, return -1. The algorithm must have O(log n) runtime complexity.
"""


def binary_search(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = left + (right - left) // 2
    if target < nums[mid]:
      right = mid - 1
    elif target > nums[mid]:
      left = mid + 1
    else:  # target == nums[mid]
      return mid
  return -1  # target not found


# test cases
nums1 = [-1,0,3,5,9,12]
target1 = 9
nums2 = [-1,0,3,5,9,12]
target2 = 2
print(f"nums={nums1} target={target1}", "Pass" if binary_search(nums1, target1) == 4 else "Fail")
print(f"nums={nums2} target={target2}", "Pass" if binary_search(nums2, target2) == -1 else "Fail")
