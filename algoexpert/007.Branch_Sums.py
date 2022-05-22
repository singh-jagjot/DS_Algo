from typing import List


class Node:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None


def branchSums(tree, sums: List, sum=0):
    if tree is None:
        return sums
    if tree.left is None and tree.right is None:
        sum += tree.value
        sums.append(sum)
        return sums
    branchSums(tree.left, sums, sum+tree.value)
    branchSums(tree.right, sums, sum+tree.value)
    return sums
