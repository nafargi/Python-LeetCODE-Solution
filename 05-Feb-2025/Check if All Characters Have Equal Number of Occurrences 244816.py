# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict_freq = Counter(s)
        freq = dict_freq[s[0]]
        
        for key in dict_freq:
           if freq !=  dict_freq[key]:
             return False
        return True
            
            