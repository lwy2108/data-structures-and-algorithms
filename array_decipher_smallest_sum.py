"""
Given an array A of alphanumeric strings, where each alphabet masks a numeric digit from 1 to 9, 
return the array of deciphered string numbers where the sum of it is smallest.

Each unique alphabet corresponds to a fixed numeric digit and there are no overlaps.

Follow-up:
What if there cannot exist any consecutive digits which are identical?  <- array_decipher_smallest_sum_non_consecutive
"""


def array_decipher_smallest_sum(n, A):
  score = {}
  for x in A:
    last_i = len(x) - 1
    for i in range(last_i, -1, -1):
      char = x[i]
      if char.isalpha():
        pos = abs(i - last_i)
        score[char] = pow(10, pos) + score.get(char, 0)
  sorted_score = sorted(score.items(), key=lambda x: x[1], reverse=True)
  for i in range(len(sorted_score)):
    char = sorted_score[i][0]
    for j in range(len(A)):
      A[j] = A[j].replace(char, str(i + 1))
  return A
          
          
# test cases
n1, A1 = 2, ["A1A", "B23"]
n2, A2 = 3, ["B3B", "B235C", "A1C"]
n3, A3 = 2, ["12A", "B23A4", "2C1"]
print(n1, A1, "Pass" if array_decipher_smallest_sum(n1, A1.copy()) == ["111", "223"] else "Fail")
print(n2, A2, "Pass" if array_decipher_smallest_sum(n2, A2.copy()) == ["131", "12353", "213"] else "Fail")
print(n3, A3, "Pass" if array_decipher_smallest_sum(n3, A3.copy()) == ["122", "12324", "231"] else "Fail")
