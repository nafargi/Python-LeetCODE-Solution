# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        st = deque([root])
        while st:
             node =st.popleft()
             if node.val >= val :
                 if node.left:
                    st.append(node.left)
                 else:
                    node.left = TreeNode(val)
                    break
             else:
                if node.right:
                    st.append(node.right)
                else:
                    node.right = TreeNode(val)
                    break
        return root

          
