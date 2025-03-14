# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        node_list = deque([root])
        ans =[]
        while node_list:
            max_val = float('-inf')
            for i in range(len(node_list)):
                node = node_list.popleft()
                max_val = max(max_val,node.val)
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            ans.append(max_val)

        return ans
                
                

        