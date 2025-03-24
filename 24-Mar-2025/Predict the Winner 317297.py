# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) -1

        def checkWinner(left,right):

            if left == right:
                return nums[left]

            start = nums[left] - checkWinner(left+1 , right)
            end = nums[right] - checkWinner(left,right-1)
            max_score = max(start,end)
            return max_score


        return checkWinner(left,right) >= 0