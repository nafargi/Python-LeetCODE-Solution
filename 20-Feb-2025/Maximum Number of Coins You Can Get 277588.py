# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        me = 0
        res = []
        n = len(piles)//3
        for i in range(1,len(piles),2):
            res.append(piles[i])
        me = sum(res[0:n])
        return me