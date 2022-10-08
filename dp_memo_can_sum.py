"""
Determine if target can be derived by summing elements of nums.

Each element can be used any number of times.
"""


def dp_memo_can_sum(target, nums):  # m = target, n = nums, T = O(n^m), S = O(m)
  if target == 0:
    return True
  for num in nums:
    if num <= target:
      if dp_memo_can_sum(target - num, nums):
        return True
  return False


def dp_memo_can_sum(target, nums, memo={}):  # m = target, n = nums, T = O(m*n), S = O(m)
  if target in memo:
    return memo[target]
  if target == 0:
    return True
  for num in nums:
    if num <= target and dp_memo_can_sum(target - num, nums, memo):
      memo[target] = True
      return True
  memo[target] = False
  return False


# test cases
target1, nums1 = 7, [2, 3]
target2, nums2 = 7, [5, 3, 4, 7]
target3, nums3 = 7, [2, 4]
target4, nums4 = 8, [2, 3, 5]
target5, nums5 = 300, [7, 14]
print(target1, nums1, "Pass" if dp_memo_can_sum(target1, nums1) else "Fail")
print(target2, nums2, "Pass" if dp_memo_can_sum(target2, nums2) else "Fail")
print(target3, nums3, "Pass" if dp_memo_can_sum(target3, nums3) else "Fail")
print(target4, nums4, "Pass" if dp_memo_can_sum(target4, nums4) else "Fail")
print(target5, nums5, "Pass" if dp_memo_can_sum(target5, nums5) else "Fail")
