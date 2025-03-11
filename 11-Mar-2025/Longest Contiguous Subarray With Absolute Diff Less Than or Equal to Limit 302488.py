# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        dq = deque()
        min_dq = deque()
        left = 0
        size = 0

        for right in range(len(nums)):
            while dq and nums[right] > dq[-1]:
                dq.pop()
            dq.append(nums[right])

            while min_dq and nums[right] < min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[right])

            while dq[0] - min_dq[0] > limit:
                if nums[left] == dq[0]:
                    dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1

            size = max(size, right - left + 1)

        return size