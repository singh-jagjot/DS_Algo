# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        def helper(root, lst):
            if not root:
                return
            helper(root.left, lst)
            helper(root.right, lst)
            lst.append(root.val)
        helper(root, lst)
        return lst
        