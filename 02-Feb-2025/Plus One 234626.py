# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      all_nums = int("".join(map(str,digits))) + 1 
      new_digits = []

      while all_nums > 0:
         new_digits.append(all_nums % 10) 
         all_nums = all_nums // 10

      reverse = new_digits[::-1]
      return  reverse
        