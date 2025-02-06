# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
            
        for _ in range(3):
            for i in range(len(mat)):
                for j in range(i+1,len(mat[0])):
                    mat[i][j],mat[j][i] =mat[j][i],mat[i][j]
            for i in range(len(mat)):
                mat[i].reverse()
            if mat == target:
                return True
        return False
