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
