# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        l = []
        for i in freq:
          for j in range(freq[i]):
            l.append(i)
    
        l.sort(key=lambda x: freq[x], reverse=True)
       
        return ''.join(l)

