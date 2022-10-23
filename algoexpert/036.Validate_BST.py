from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value: Any = value
        self.left = None
        self.right = None


def validate_bst(root: Node) -> bool:
    def helper(root: Node, minval, maxval):
        if root is None:
            return True
        if root.value < minval or root.value >= maxval:
            return False
        return helper(root.left, minval, root.value) and helper(root.right, root.value, maxval)
    helper(root, float("-inf"), float("inf"))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
