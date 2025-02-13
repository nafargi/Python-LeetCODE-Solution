# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        ws = len(p) 
        dict1 = Counter(p)
        dict2 = Counter(s[:ws-1])

        if  dict1  == dict2:
            ans.append(0)
            
        for i in range(ws-1,len(s)):
            dict2[s[i]] += 1

            if dict1 == dict2:
                ans.append(i-ws+1)

            dict2[s[i-ws +1]] -= 1
            
            if dict2[s[i-ws+1]] == 0:
                    del dict2[s[i-ws+1]]
                
            
                
        return ans