# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = []
        return targetSum in self.branchSums(root, sums)
    
    def branchSums(self, tree, sums, sum = 0):
        if tree is None:
            return sums
        if tree.left is None and tree.right is None:
            sum+=tree.val
            sums.append(sum)
            return sums
        self.branchSums(tree.left, sums, sum+tree.val)
        self.branchSums(tree.right, sums, sum+tree.val)
        return sums