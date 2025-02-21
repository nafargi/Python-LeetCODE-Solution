# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        diff = [0] * (n + 1)  

        for i in range(len(shifts)):
            if shifts[i][2] == 1:
              diff[shifts[i][0]] += 1
              diff[shifts[i][1]+1] -= 1
            else:
              diff[shifts[i][0]] -= 1
              diff[shifts[i][1]+1] += 1
            

        shift = 0
        result = []

        for i in range(n):
            shift += diff[i]
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
            result.append(new_char)

        return "".join(result)
