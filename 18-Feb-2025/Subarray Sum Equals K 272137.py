# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0 
        counter = 0 
        
        freq_count = {0:1}

        for i in nums:
            pre_sum += i
            
            if pre_sum - k in freq_count:
                counter += freq_count[pre_sum - k]
            if pre_sum in freq_count:
                freq_count[pre_sum] += 1
            else:
                freq_count[pre_sum] = 1
        return counter