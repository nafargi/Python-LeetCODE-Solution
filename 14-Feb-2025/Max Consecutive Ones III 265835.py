# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        zero_counter = k
        max_len= 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zero_counter -= 1

            while zero_counter < 0:
                
                if nums[left] == 0:
                    zero_counter += 1
                left += 1
            
            max_len = max(max_len,right-left+1)

        return max_len