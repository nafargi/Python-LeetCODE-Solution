# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
      l = 0
      r =0
      count = 0
      for i in range(len(s)):
         if s[i] == 'R':
            r += 1
         else:
            l += 1
          
         if r == l:
            count += 1
      return count
