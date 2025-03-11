# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        count = 1
        ans.append(count)

        for i in range(1,rowIndex +1):
            count = count * (rowIndex - i + 1)
            count = count // i
            ans.append(count)
        return ans