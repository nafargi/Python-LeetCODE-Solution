# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        total = sum(weights)
        max_weight = max(weights)

        while max_weight < total:
            mid = (total + max_weight) // 2
            curr_weight = 0
            day = 1

            for weight in weights:
                if curr_weight + weight > mid:
                    day += 1  
                    curr_weight = 0  
                curr_weight += weight

            if day > days:
                max_weight = mid + 1
                min_capacity = mid + 1
            else:
                total = mid 
                
        return  max_weight


            


