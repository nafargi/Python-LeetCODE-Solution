# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            self.total =0
            def dfs(root,curr):
                curr = (10*curr) + root.val
                if not root.left and not root.right:
                    self.total += curr
                
                if root.left:
                    dfs(root.left,curr)
                if root.right:
                    dfs(root.right,curr)
            dfs(root,0)
            return self.total