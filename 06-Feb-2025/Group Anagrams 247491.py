# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [] 
        temp = []
        sorted_strs = [0] * len(strs)
        for i in range(len(strs)):
            sorted_strs[i] = ''.join(sorted(strs[i]))
        
        for i in range(len(strs)):
            
            if strs[i] in temp:
               continue
            group = [strs[i]]
            for j in range(i+1,len(strs)):
                if sorted_strs[i] == sorted_strs[j] :
                    group.append(strs[j])
            ans.append(group)
            temp.extend(group)
        return ans