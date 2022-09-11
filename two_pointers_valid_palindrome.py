"""
Given a string s, return true if it is a palindrome, or false otherwise.
"""


def two_pointers_valid_palindrome(s):
  s = [i.lower() for i in s if i.isalnum()]
  for i in range(len(s)):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True


# test cases
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
print(f"\"{s1}\"", "Pass" if two_pointers_valid_palindrome(s1) is True else "Fail")
print(f"\"{s2}\"", "Pass" if two_pointers_valid_palindrome(s2) is False else "Fail")
print(f"\"{s3}\"", "Pass" if two_pointers_valid_palindrome(s3) is True else "Fail")
