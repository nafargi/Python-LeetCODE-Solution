# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l = 0
        r = len(people)-1

        while l <= r:
            left = people[l]
            right = people[r]
            if l == r:
                l += 1
            elif left + right <=limit:
                l += 1
                r -= 1
            else:
                r -= 1
            
            boats += 1
        
        return boats