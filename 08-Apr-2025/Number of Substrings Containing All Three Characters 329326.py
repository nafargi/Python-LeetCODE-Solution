# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [-1, -1, -1]
        count, right = 0, 0
        while right < len(s):
            abc[ord(s[right]) - ord('a')] = right
            minIndex = min(abc)
            count += (minIndex + 1)
            right += 1
        return count