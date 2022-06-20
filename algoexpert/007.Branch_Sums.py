from typing import List


class Node:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.left = None
        self.right = None


def branch_sums(tree, sums: List, total=0):
    if tree is None:
        return sums
    if tree.left is None and tree.right is None:
        total += tree.value
        sums.append(total)
        return sums
    branch_sums(tree.left, sums, total + tree.value)
    branch_sums(tree.right, sums, total + tree.value)
    return sums
