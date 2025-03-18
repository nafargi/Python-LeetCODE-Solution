# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        st = deque([root])
        p_root = None
        while st:
            node =st.popleft()

            if node.val == key :
                #case:1 for no children
                if not node.left and not node.right:
                    if p_root:
                        if p_root.left == node:
                           p_root.left = None
                        else:
                            p_root.right = None
                    else:
                        return None
                #case:2 one right children
                elif not node.left:
                    if p_root:
                        if p_root.left == node:
                           p_root.left = node.right
                        else:
                           p_root.right = node.right
                    else:
                        return node.right

                #case:3 one left children
                elif not node.right:
                    if p_root:
                        if p_root.left == node:
                           p_root.left = node.left
                        else:
                            p_root.right = node.left
                    else:
                        return node.left
                #case:4 node has two children
                else:
                    suc_parent = node
                    cur_suc = node.right
                    while cur_suc.left:
                        suc_parent = cur_suc
                        cur_suc = cur_suc.left

                    node.val = cur_suc.val

                    if suc_parent.left == cur_suc:
                        suc_parent.left = cur_suc.right
                    else:
                        suc_parent.right = cur_suc.right

                break 
            elif node.val > key:
                if node.left:
                    p_root= node
                    st.append(node.left)
            else:
                if node.right:
                    p_root= node
                    st.append(node.right)
        return root



        

          
