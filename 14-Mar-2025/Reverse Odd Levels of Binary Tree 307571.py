# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        odd_counter = 0
        node_list = deque([root])

        while node_list:

            if odd_counter % 2 != 0:
               temp = [node.val for node in node_list]
               temp.reverse()

               for i, node in enumerate(node_list):
                    node.val = temp[i]
               
            for i in range(len(node_list)):
                node = node_list.popleft()
                if node.left:
                    node_list.append(node.left)
                if node.right:
                    node_list.append(node.right)
            odd_counter += 1

        return root

            

