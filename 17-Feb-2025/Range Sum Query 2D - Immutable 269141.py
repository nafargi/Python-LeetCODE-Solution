# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[]
        for row in range(len(matrix)):
            temp = []
            presum = 0
            for col in range(len(matrix[0])):
                presum += matrix[row][col]
                temp.append(presum)
            self.prefix.append(temp)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res= 0 
        for i in range(row1,row2+1):
            if col1==0:
                res += self.prefix[i][col2] 
            else:
                res += self.prefix[i][col2] - self.prefix[i][col1-1]
        return res
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)