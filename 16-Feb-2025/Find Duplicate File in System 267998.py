# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths):
        dict1, result = defaultdict(list), []

        for i in paths:
            ans = i.split()
            for j in ans[1:]:
                l_idx, r_idx = j.index("("), j.index(")")
                dict1[j[l_idx+1:r_idx]].append(ans[0]+"/"+j[:l_idx])

        for key,val in dict1.items():
            if len(val) > 1:
                result += [val]

        return result 

        
        