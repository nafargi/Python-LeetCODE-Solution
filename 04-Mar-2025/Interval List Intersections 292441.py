# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        merged = firstList+secondList
        merged = sorted(merged,key=lambda x:x[0])
        res= []
        start, end = merged[0][0],merged[0][1]
        i=1
        while i < len(merged):
            if end>=merged[i][1]:
                res.append([merged[i][0],merged[i][1]])
                i+=1

            elif end>=merged[i][0]:
                res.append([merged[i][0],end])
                start=end
                end=merged[i][1]
                i+=1
            else:
                start=merged[i][0]
                end=merged[i][1]
                i+=1
        return res