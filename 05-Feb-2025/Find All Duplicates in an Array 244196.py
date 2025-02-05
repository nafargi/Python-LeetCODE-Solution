# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dicts = Counter(nums)
        nums.clear()
        
        for key in dicts:
            if dicts[key] >=2:
                nums.append(key)
        return nums