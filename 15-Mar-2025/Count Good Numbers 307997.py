# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def pow(x, n):
            if n == 0: return 1
            if n == 1: return x
            if n % 2 == 0: 
                ans = pow(x, n / 2)
                return (ans * ans) % MOD
            else:
                ans = pow(x, (n - 1) / 2)
                return (x * ans * ans) % MOD

        eve_count = n // 2
        odd_count = n - eve_count

        res = ((pow(4, eve_count) % MOD * pow(5, odd_count) % MOD) % MOD)
        return res