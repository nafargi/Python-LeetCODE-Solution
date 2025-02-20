# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1 = {}
        for i in s1:
            if i in dicts1:
                dicts1[i] += 1
            else:
                dicts1[i] = 1
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        t = {}
        for i in range(n): 
            if s2[i] in t:
                t[s2[i]] += 1
            else:
                t[s2[i]] = 1
        if t == dicts1:
            return True
        for i in range(n, m):  
            j = s2[i - n]
            t[j] -= 1
            if t[j] == 0:
                del t[j]
            k = s2[i]
            if k in t:
                t[k] += 1
            else:
                t[k] = 1
            if t == dicts1:
                return True
        return False