# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = []
        t = deque([[root, 0]])

        while t:
            nd, h = t.popleft()

            if nd:
                value = nd.val
            else:
                value = None


            if len(ans) == h:
                ans.append([value])
            else:
                ans[h].append(value)

            if nd: 
                t.append([nd.left, h+1])
                t.append([nd.right, h+1])

        for i in ans:
            if i != i[::-1]: 
                return False

        return True
            