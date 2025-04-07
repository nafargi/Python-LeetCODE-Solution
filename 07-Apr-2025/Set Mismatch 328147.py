# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set_nums = set((nums))
        dpl = sum(nums) - sum(set_nums)
        n = len(nums)
        ans = ( n * (n + 1) // 2 ) - sum(set_nums)

        return [dpl, ans]