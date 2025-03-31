# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, dif, sum):
            p = len(queens)
            if p == n:
                self.result += 1
                return None
            for q in range(n):
                if q not in queens and p-q not in dif and p+q not in sum:
                    dfs(queens+[q], dif+[p-q], sum+[p+q])
        
        self.result = 0
        dfs([],[],[])
        return self.result