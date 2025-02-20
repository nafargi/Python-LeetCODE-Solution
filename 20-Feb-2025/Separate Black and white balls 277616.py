# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        n, res = len(s), 0
        l = r = n - 1
        while l >= 0:
            if s[l] == "1":
                res += r - l
                r -= 1
            l -= 1
        return res