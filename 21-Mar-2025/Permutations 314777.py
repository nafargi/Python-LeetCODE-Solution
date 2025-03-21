# Problem: Permutations - https://leetcode.com/problems/permutations/

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        visited = [False] * len(nums)  # To track if an element is visited
        
        def backtrack():
            if len(temp) == len(nums):  # If the current permutation is complete
                ans.append(temp[:])  # Add a copy of the current permutation to the result
                return

            for i in range(len(nums)):
                if visited[i]:  # Skip if the element is already used
                    continue

                visited[i] = True  # Mark the current element as used
                temp.append(nums[i])  # Add the element to the current permutation
                backtrack()  # Recurse to build the next level
                temp.pop()  # Backtrack (remove the last element)
                visited[i] = False  # Mark the current element as unused

        backtrack()
        return ans

# Example usage:
sol = Solution()
print(sol.permute([1, 2, 3]))
