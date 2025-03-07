# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
         s = []

         for i in range(len(logs)):
            if logs[i] == "../" and s != []:
                s.pop()
            elif logs[i]=="./" or logs[i]=="../" and s == []:
                continue
            else:
                s.append(logs[i])
         return len(s)

        