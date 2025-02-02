# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        sums = 0
        i = 0
        ans = 0
        for j in range(len(nums)):
            sums += nums[j]
            while nums[j]*(j-i+1) > sums+k:
                sums -= nums[i]
                i = i+1
            ans = max(ans, j-i+1)
        return ans