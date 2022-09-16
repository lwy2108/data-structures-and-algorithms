"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid (every close bracket has a corresponding open bracket of the same type).
"""


def stack_valid_parentheses(s):
  opening = ['(', '{', '[']
  closing = [')', '}', ']']
  stack = []
  for char in s:
    if char in opening:
      stack.append(opening.index(char))
    elif stack and char in closing:
      if closing.index(char) == stack[-1]:
        stack.pop()
      else:
        return False
    else:  # if not stack and char in closing
      return False
  return True


# test cases
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
print(s1, "Pass" if stack_valid_parentheses(s1) else "Fail")
print(s2, "Pass" if stack_valid_parentheses(s2) else "Fail")
print(s3, "Pass" if stack_valid_parentheses(s3) is False else "Fail")
print(s4, "Pass" if stack_valid_parentheses(s4) else "Fail")
