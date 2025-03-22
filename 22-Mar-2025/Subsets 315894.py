# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def generateSubsets(self, index, ans, nums, seen, subset):
        if index == len(nums):
            subset_tuple = tuple(subset)  # Convert list to tuple for set storage
            if subset_tuple not in seen:
                ans.append(list(subset))
                seen.add(subset_tuple)
            return
        
        # Include current element
        subset.append(nums[index])
        self.generateSubsets(index + 1, ans, nums, seen, subset)
        
        # Exclude current element
        subset.pop()
        self.generateSubsets(index + 1, ans, nums, seen, subset)

    def subsets(self, nums):
        ans = []
        seen = set()
        self.generateSubsets(0, ans, nums, seen, [])
        return ans