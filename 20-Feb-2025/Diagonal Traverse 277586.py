# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        if n == 1:
            return [a[0] for a in mat]
        if m == 1:
            return mat[0]
        
        start_points = [(0,j) for j in range(n)] 

        start_points += [(i,n-1) for i in range(1,m)] 
        res = []

        for (si,sj) in start_points:

            i,j = si,sj
            diag_order = []

            while 0 <= i < m and 0 <= j < n:

                diag_order.append(mat[i][j])

                i += 1
                j -= 1

            if (si+sj) % 2 == 0:
                diag_order.reverse()

            res += diag_order

        return res