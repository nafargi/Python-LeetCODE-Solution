# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
            row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
            row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
            row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
            ans = []

            for i in range(len(words)):
                if set(words[i].lower()).issubset(row1) or set(words[i].lower()).issubset(row2) or set(words[i].lower()).issubset(row3):
                    ans.append(words[i])
            return ans
 