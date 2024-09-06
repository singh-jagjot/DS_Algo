# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) Time, O(n) space
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        issuccessor = False
        successor = None

        def helper(node):
            nonlocal issuccessor, successor
            if not node:
                return
            helper(node.left)
            if issuccessor and not successor:
                if node:
                    successor = node
            if node.val == p.val:
                issuccessor = True
            helper(node.right)
        helper(root)
        return successor


# Better Solution: O(n) time, O(h) space
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        while root:
            # Ignoring the left side of the tree as successor can't be there beacuse
            # in inorder we could have already visited it.
            if root.val <= p.val:
                root = root.right
            else:
                # Potential successor as it will be the left most node of the right subtree
                successor = root
                root = root.left
        return successor
