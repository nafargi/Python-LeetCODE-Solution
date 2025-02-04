# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        ans = [None] * n
        for i in range(n):
            index = (nums[i] + i) % n
            ans[i] = nums[index]
        return ans