# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = sorted(nums)

        for i in range(len(nums)):
          nums[i] = count.index(nums[i])
    
        return nums