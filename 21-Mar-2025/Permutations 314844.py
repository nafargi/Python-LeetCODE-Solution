# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            ans = []
            temp = []
            
            def backtrack(temp,nums):
                if len(temp) == len(nums):
                    ans.append(temp[:])
                    return

                for i in range(len(nums)):
                    if nums[i] in temp:
                        continue
                    temp.append(nums[i])
                    backtrack(temp,nums)
                    temp.pop()
                
            backtrack(temp,nums)
            return ans
            
