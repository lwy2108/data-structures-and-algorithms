"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""


def string_valid_anagram(s, t):
  return sorted(s) == sorted(t)


# test cases
s1, t1 = "anagram", "nagaram"
s2, t2 = "rat", "car"
print(s1, t1, "Pass" if string_valid_anagram(s1, t1) is True else "Fail")
print(s2, t2, "Pass" if string_valid_anagram(s2, t2) is False else "Fail")
