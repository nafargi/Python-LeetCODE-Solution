# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
      def black(n):
        return nums[n] < minK or nums[n] > maxK
      def red(n):
        return nums[n] == minK
      def blue(n):
        return nums[n] == maxK

      count = 0
      start = 0

      nums.append(minK-1)
      while True:
        while start < len(nums) and black(start):
          start += 1

        if start == len(nums):
          break
        end = start

        if minK == maxK:
          while not black(end):
            end += 1
          l = end - start

          count += (l * (l+1)) // 2
          start = end + 1
          continue

        r = b = None  
        while True:
          if black(end) or red(end) or blue(end):
            
            if r != None and b != None:

              large = max(r, b)
              small = min(r, b)

              count += (small-start+1) * (end-large)
            if red(end):
              r = end
            elif blue(end):
              b = end
            elif black(end):
              break
          end +=1
        start = end + 1
      return count