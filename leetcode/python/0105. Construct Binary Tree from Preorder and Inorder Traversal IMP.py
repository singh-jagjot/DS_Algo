# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        inmap = {v: i for i, v in enumerate(inorder)}
        preorderidx = 0

        def helper(left, right):
            nonlocal preorderidx
            if left > right:
                return
            rootval = preorder[preorderidx]
            # With this because after every recursive call, preorder[preorderidx] is a root for it's own tree
            preorderidx += 1
            node = TreeNode(rootval)
            node.left = helper(left, inmap[rootval] - 1)
            node.right = helper(inmap[rootval] + 1, right)
            return node
        return helper(0, len(preorder) - 1)
