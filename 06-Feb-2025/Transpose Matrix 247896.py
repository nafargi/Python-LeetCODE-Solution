# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
                trans_mtrx = [[] for _ in range(len(matrix[0]))] 

                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        trans_mtrx[j].append(matrix[i][j])         
                return trans_mtrx