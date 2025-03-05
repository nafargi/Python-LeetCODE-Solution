# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums):
        n = len(nums)
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        # Kadane's algorithm to find max and min subarray sums
        for i in range(1, n):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            min_ending_here = min(nums[i], min_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
            min_so_far = min(min_so_far, min_ending_here)
        
        # The maximum absolute sum is the maximum of the absolute values of max_so_far and min_so_far
        return max(abs(max_so_far), abs(min_so_far))