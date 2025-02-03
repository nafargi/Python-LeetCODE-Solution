# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         pairs = {}

         for i , num in enumerate(nums):
            val = target - num
            if val in pairs:
                return [i, pairs[val]]
            pairs[num] = i
         return []
