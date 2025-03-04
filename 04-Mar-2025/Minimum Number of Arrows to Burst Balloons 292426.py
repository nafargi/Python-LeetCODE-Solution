# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[1])
        ans ,arr = 0,0

        for [s,e] in points:
            if ans == 0 or s > arr:
                ans , arr = ans +1, e
        return ans


