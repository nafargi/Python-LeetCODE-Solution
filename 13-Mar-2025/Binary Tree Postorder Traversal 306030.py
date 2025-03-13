# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class Solution:
  def postorderTraversal(self, root: TreeNode | None) -> list[int]:
    ans = []

    def post_order(root: TreeNode | None) -> None:
      if not root:
        return

      post_order(root.left)
      post_order(root.right)
      ans.append(root.val)

    post_order(root)
    return ans