# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def check(l, i, j):
            if j == n and l != 0:
                return True
            if len(str(int(num[l:i]))) != i - l:
                return False
            if len(str(int(num[i:j]))) != j - i:
                return False
            st = str(int(num[l:i]) + int(num[i:j]))
            if j + len(st) > n:
                return False
            elif st == num[j:j+len(st)]:
                return check(i, j, j + len(st))
        for i in range(1, n-1):
            for j in range(i+1, n):
                if check(0, i, j):
                    return True
        
        return False