# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = []
        t = collections.deque([[root, 0]])

        while t:
            nd, level = t.popleft()

            if nd:
                value = nd.val
            else:
                value = None


            if len(ans) == level:
                ans.append([value])
            else:
                ans[level].append(value)

            if nd: 
                t.append([nd.left, level+1])
                t.append([nd.right, level+1])

        for i in ans:
            if i != i[::-1]: 
                return False

        return True
            