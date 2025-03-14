# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        st = deque([(root,root.val,root.val)])
        max_diff = 0

        while st:

            node, min_val, max_val = st.popleft()
            max_diff = max(max_diff, abs(max_val - min_val))
            
            if node.left:

                    cur_max = max(max_val,node.left.val)
                    cur_min = min(min_val,node.left.val)
                    st.append((node.left,cur_min,cur_max))

            if node.right:

                    cur_max = max(max_val,node.right.val)
                    cur_min = min(min_val,node.right.val)
                    st.append((node.right,cur_min,cur_max))

        return max_diff
           


        