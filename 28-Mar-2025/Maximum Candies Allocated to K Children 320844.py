# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        high = max(candies)
        low = 1

        while low <= high:
            mid = (low + high) // 2
            curr_k = 0
            
            
            for i in candies:
                curr_k += i // mid
                if curr_k >= k:
                    break

            if curr_k >= k:
               low = mid + 1
            else:
                high = mid -1

        return high



