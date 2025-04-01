# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = (right + left) // 2

            if  matrix[mid][0] <= target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[mid])-1

                while l <= r:
                    md = (l + r) // 2

                    if matrix[mid][md] == target:
                        return True
                    elif matrix[mid][md] < target:
                        l = md + 1
                    else:
                        r = md - 1
                return False

            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
      
            


