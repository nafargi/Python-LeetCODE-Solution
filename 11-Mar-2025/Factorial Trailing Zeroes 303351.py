# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            return n // 5 + self.trailingZeroes(n // 5)
