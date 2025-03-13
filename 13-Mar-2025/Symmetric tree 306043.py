# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        sub_list = []
        level = deque([[root, 0]])

        while level:
            curr_nd, h = level.popleft()

            if curr_nd:
                num = curr_nd.val
            else:
                num = None


            if len(sub_list) == h:
                sub_list.append([num])
            else:
                sub_list[h].append(num)

            if curr_nd: 
                level.append([curr_nd.left, h+1])
                level.append([curr_nd.right, h+1])

        for i in sub_list:
            if i != i[::-1]: 
                return False

        return True
            