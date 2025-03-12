# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dq = deque()
       
        for i in range(1,n+1):
         dq.append(i)
        while len(dq) > 1:
            for i in range(k-1):
                 dq.append(dq.popleft())
            dq.popleft()
        return dq[0]