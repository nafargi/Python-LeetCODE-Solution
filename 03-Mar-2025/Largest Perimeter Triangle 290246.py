# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1,1,-1):
            c = nums[i-1] + nums[i-2]

            if c > nums[i]:
                return c + nums[i]
        return 0
