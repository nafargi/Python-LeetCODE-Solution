# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            ans = []

            def pre_order(root: TreeNode | None) -> None:
                if not root:
                    return
                    
                ans.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
            pre_order(root)
            return ans