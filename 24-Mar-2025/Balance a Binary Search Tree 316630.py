# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self ,root):
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        values = inorder(root)
        
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(values[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(values) - 1)