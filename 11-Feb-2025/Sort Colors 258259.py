# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * (max(nums)+1)
        j = 0

        for i in range(len(nums)):
            count[nums[i]] += 1

        for i in range(len(count)):
            for _ in range(count[i]):
                nums [j] = i
                j += 1

            
        