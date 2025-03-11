# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for x in tokens:
            if x == '+':
                val = st[-2] + st[-1]   
                st.pop()
                st.pop()
                st.append(val)
                
            elif x == '-':
                val = st[-2] - st[-1]
                st.pop()
                st.pop()
                st.append(val)
                
            elif x == '*':
                val = st[-2] * st[-1]
                st.pop()
                st.pop()
                st.append(val)
                
            elif x == '/':
                val = int(st[-2] / st[-1])
                st.pop()
                st.pop()
                st.append(val)
                
            else:
                st.append(int(x))
            
        
            
        return st[-1]


        