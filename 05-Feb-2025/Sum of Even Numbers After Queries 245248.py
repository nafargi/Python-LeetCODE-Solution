# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
         
          ans = [0] * len(nums)
          for i in range(len(queries)):
             nums[queries[i][1]] += queries[i][0]
             for j in range(len(nums)):
                if nums[j] % 2 == 0:
                    ans[i] += nums[j]
          return ans


