# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0: return
        if k > len(nums):
            k = k % len(nums)
        n = len(nums) - k
        temp = nums[:n]
        nums[:k] = nums[n:]  
        nums[k:] = temp
