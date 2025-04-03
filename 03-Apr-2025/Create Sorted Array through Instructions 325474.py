# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        nums = []
        cost = 0

        for i in range(len(instructions)):
            left = 0
            right = len(nums) -1
            min_num = 0
            max_num = 0
           
            while left <= right:
                    mid = (left + right) // 2
                    if instructions[i] > nums[mid]:
                         left = mid + 1
                    else:
                        right = mid - 1
            min_num = left

            left, right = 0, len(nums)-1
            while left <= right:
                    mid = (left + right) // 2
                    if instructions[i] >= nums[mid]:
                         left = mid + 1
                    else:
                        right = mid - 1
            max_num = len(nums) - left    

            cost += min(min_num,max_num)
            nums.insert(min_num ,instructions[i])

        return cost % (10**9 + 7)


            


        