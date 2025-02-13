# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        widz = 0
        area = 0

        while i < j:
            widz = j - i 
            temp =widz *  min(height[i],height[j])
            area = max(area, temp)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return area
        
        