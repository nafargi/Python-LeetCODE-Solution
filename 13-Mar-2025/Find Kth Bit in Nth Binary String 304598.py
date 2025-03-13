# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            chr = ''
            for i in s:
                if i == '0':
                    chr += '1'
                else:
                    chr += '0'
            return chr

        def inverter(n):
            if n == 1:
                return '0'
            return inverter(n-1) + '1' + invert(inverter(n-1))[::-1]
        
        ans = inverter(n)
        return ans[k-1]

