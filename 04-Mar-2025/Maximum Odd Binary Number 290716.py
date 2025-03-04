# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
      ans = [0]* len(s)
      count = s.count('1')

      for i in range(count-1):
         ans[i] = 1
      ans[len(s)-1] = 1
      ans =  "".join(map(str,ans))
      return ans