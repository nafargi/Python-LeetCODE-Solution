# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = []
        last = 0
        j = 0

        for i in range(len(s)):
            last = max(last,s.rindex(s[i]))
            if i == last:
                l.append(i-j+1)
                j = i + 1
            
        return l