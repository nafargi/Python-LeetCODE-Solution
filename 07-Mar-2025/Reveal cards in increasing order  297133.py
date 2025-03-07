# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        q = list(range(len(deck)))
        ans = [0]*len(deck)

        i = 0
        while q != []:
            if len(q) == 1:
                ans[q[0]]=deck[i]
                q.remove(q[0])
            else:
                top = q[0]
                last = q[1]
                q.remove(q[1])
                q.remove(q[0])
                q.append(last)
                ans[top]= deck[i]
            
            i += 1
    
        return ans
                