# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        isComment = False        
        line = ''                
        
        for s in source:
            n = len(s)
            i = 0

            while i < n:
                if not isComment:

                    if i + 1 < n  and s[i: i + 2] == '//':
                        break

                    elif i + 1 < n and s[i: i + 2] == '/*':
                        isComment = True      
                        i += 1                 

                    else:
                        line += s[i]

                else:
                    if i + 1 < n and s[i: i + 2] == '*/':
                        isComment = False       
                        i += 1                 
                
                i += 1

            if not isComment and line:
                res += [line]
                line = ''            

        return res