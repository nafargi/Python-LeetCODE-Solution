# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
         dict_nums = Counter(nums)
         ans = []

         for k in dict_nums:
            if dict_nums[k] >= 2:
              ans.append(k)
         return ans