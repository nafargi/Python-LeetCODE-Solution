# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, A):
        res = []
        
        def flip(k):
            A[:k] = A[:k][::-1]
        
        for size in range(len(A), 1, -1):
            max_idx = A.index(max(A[:size]))
            if max_idx == size - 1:
                continue
            if max_idx != 0:
                res.append(max_idx + 1)
                flip(max_idx + 1)
            res.append(size)
            flip(size)
        
        return res