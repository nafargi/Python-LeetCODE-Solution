# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        p = 0
        
        for i in range(n + 1):
            sqr_vl = i * i
            s = str(sqr_vl)
            
            if self.check(s, i, 0, 0):
                p += sqr_vl
        
        return p 

    def check(self, num_str, target, index, current_sum) :

        if index == len(num_str):
            return current_sum == target
        
        sum_value = 0
        
        for i in range(index, len(num_str)):
            sum_value = sum_value * 10 + (ord(num_str[i]) - ord('0'))
            
            if sum_value + current_sum > target:
                break
            
            if self.check(num_str, target, i + 1, current_sum + sum_value):
                return True
        
        return False