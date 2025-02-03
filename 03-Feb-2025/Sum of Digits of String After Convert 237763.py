# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for i in range(len(s)):
            string += str(ord(s[i]) - 96)
        while k > 0:
            sum_ = 0
            for num in string:
                sum_ += int(num)
            k-=1
            string = str(sum_)
        return sum_