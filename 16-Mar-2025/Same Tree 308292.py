# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False            
        p_st = deque([p])
        q_st= deque([q])
    
        while p_st and q_st:
            p_lev = []
            q_lev = []

            for _ in range(len(p_st)):
                p_node = p_st.popleft()
                q_node = q_st.popleft()
                 
                if not p_node and not q_node :
                    continue
                if not p_node or not q_node or q_node.val != p_node.val:
                    return False
                
                p_lev.append(p_node.val)
                q_lev.append(q_node.val)
                
                p_st.append(p_node.left)
                q_st.append(q_node.left)

                p_st.append(p_node.right)
                q_st.append(q_node.right)

            if p_lev != q_lev:
                return False                    
                    
        return len(p_st) == len(q_st)
