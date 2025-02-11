# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if i!= j and str(nums[i]) +str(nums[j]) > str(nums[j]) +str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
    
        ans= "".join(str(i) for i in nums)

        if ans[0] == '0':
            return "0"
        return ans