# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_list = deque([root])
        ans =[]
        rev = False

        while node_list:
            lev = []
            for _  in range(len(node_list)):
                node = node_list.popleft()
                lev.append(node.val)

                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            if rev:
                lev.reverse()
            ans.append(lev)
            rev = not rev
        return ans