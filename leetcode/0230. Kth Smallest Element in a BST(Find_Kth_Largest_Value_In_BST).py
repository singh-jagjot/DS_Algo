# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def helper(root):
            if not root or len(arr) == k:
                return None
            helper(root.left)
            arr.append(root.val)
            helper(root.right)
        
        helper(root)
        return arr[k - 1]


# Best Solution(Iterative)
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

