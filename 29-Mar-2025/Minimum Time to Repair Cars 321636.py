# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * (cars ** 2)

        def isValid(time):
            total = 0
            for rank in ranks:
                curr_rep = int((time / rank) ** 0.5)
                total += curr_rep
                if total >= cars:
                    return True
            return False


        while left < right:
            time = (left + right) // 2
            if isValid(time):
                right = time
            else:
                left = time + 1

        return left