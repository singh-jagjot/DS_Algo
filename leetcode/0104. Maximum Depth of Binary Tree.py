# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthCal(root)
        
    def maxDepthCal(self, node, depth = 1):
        if node is None:
            return depth - 1
        return max(self.maxDepthCal(node.left, depth+1), self.maxDepthCal(node.right, depth+1))
    