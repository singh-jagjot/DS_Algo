# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def helper(node):
            nonlocal diameter
            if not node:
                return -1
            left = helper(node.left) + 1
            right = helper(node.right) + 1
            diameter = max(diameter, left + right)
            return max(left, right)

        helper(root)
        return diameter
