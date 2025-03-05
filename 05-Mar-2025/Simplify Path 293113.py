# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split('/')
        st = []
        
        for i in range(len(dir)):
            if dir == [] or dir[i] == '.':
                continue

            if dir[i] == '..':
                if st != []:
                    st.pop()
            elif dir[i] != '':
                st.append(dir[i])
    
        return '/' + '/'.join(st)

