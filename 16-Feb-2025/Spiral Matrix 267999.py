# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 0,0 -> 0,1 -> 0,2
        order = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        m,n = len(matrix),len(matrix[0])
        starting_pattern = 0
        ret = []
        i,j = 0,0

        while len(visited) != m*n:
            ret.append(matrix[i][j])
            visited.add((i,j))

            nxt_moves = order[starting_pattern]
            nxt_i = i + nxt_moves[0]
            nxt_j = j + nxt_moves[1]

            if nxt_i < 0 or nxt_i >= m or nxt_j < 0 or nxt_j >= n or (nxt_i, nxt_j) in visited:
                starting_pattern = (starting_pattern+1) % len(order)
                nxt_moves = order[starting_pattern]
                nxt_i = i + nxt_moves[0]
                nxt_j = j + nxt_moves[1]
            
            i = nxt_i
            j = nxt_j
        return ret
        