# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

    
        while left <= right:
            mid =(right + left ) // 2

            if target == nums[mid] :
                return mid 
            
            if target >= nums[mid] :
                left = mid +1
            else:
                right = mid -1
        return -1
           


