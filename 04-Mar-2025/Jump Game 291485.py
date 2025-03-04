# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        max_d = 0

        for i in range(len(nums)):
            if nums[i] + i >= target:
                return True
            if nums[i] == 0 and nums[i] + i == max_d:
                return False
            max_d = max(nums[i] + i,max_d)

        return False