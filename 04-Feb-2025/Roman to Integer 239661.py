# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dict ={"I":1,"V":5,"X":10,"L": 50,"C":100,"D":500,"M":1000}
        ans = 0
        n = len(s)
        for  i in range(n):
            if i < n - 1 and dict[s[i]] < dict[s[i + 1]]:
                ans -= dict[s[i]]
            else:
                ans += dict[s[i]]
        return ans