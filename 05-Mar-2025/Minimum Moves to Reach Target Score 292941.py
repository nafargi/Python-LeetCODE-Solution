# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        while maxDoubles and  target > 1:
            if target%2 == 0 and maxDoubles :
                c+=1
                maxDoubles-=1
                target //=2
            else:
                target -=1
                c+=1
        if target>1:
            c+=target-1
        return c 
                