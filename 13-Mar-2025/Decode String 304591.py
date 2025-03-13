# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for i in s:
            if i != "]":
                st.append(i)
            else:
                chr = ''
                while st and st[-1] != '[':
                    chr = st.pop() + chr
                st.pop()

                num = ''
                while st and st[-1].isdigit():
                    num = st.pop() + num
                st.append(chr * int(num))
                
        return "".join(st)