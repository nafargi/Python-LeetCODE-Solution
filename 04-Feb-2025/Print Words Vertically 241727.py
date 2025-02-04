# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
          letters = s.split()
          list_words = []
          ans = []
          max_size = len(max(letters, key=len))


          for i in range(max_size):  

            for j in range(len(letters)):

                if i < len(letters[j]): #check if i index exist in the current word
                    list_words.append(letters[j][i])
                else:
                    list_words.append(" ")
            ans.append("".join(list_words).rstrip())
            list_words.clear()

          return ans