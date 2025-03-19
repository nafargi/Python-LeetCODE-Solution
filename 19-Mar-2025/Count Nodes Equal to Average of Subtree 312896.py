# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.counter = 0
       
        def dfs(root,i):
            if not root:
                return 0,0

            left_sum ,left_len = dfs(root.left,i+1)
            right_sum ,right_len = dfs(root.right,i+1)

            total = root.val + left_sum + right_sum
            len = 1 + left_len + right_len

            avg = total // len

            if avg == root.val:
                self.counter += 1
                
            return total , len
            
        dfs(root,1)

        return self.counter

