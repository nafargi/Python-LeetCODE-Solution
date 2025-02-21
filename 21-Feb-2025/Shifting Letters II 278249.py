# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # Difference array

        # Apply shifts using difference array
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # Compute prefix sum to get final shift values
        shift = 0
        result = []

        for i in range(n):
            shift += diff[i]
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
            result.append(new_char)

        return "".join(result)
