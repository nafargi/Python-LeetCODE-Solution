# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        
        ans = [0] * len(nums)
        counter = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                ans[counter] = nums[i]
                counter += 1
        return ans