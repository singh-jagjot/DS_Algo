# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter) -> None:
        self.diameter = diameter

# O(n) time | O(h) space
def binaryTreeDiameter(tree):
    # Write your code here.
    treeInfo = TreeInfo(0)
    binaryTreeDiameter_(tree, treeInfo)
    return treeInfo.diameter


def binaryTreeDiameter_(node: BinaryTree, treeInfo: TreeInfo):
    if node is None:
        return -1
    left = binaryTreeDiameter_(node.left, treeInfo) + 1
    right = binaryTreeDiameter_(node.right, treeInfo) + 1
    currentDiameter = left + right
    treeInfo.diameter = max(treeInfo.diameter, currentDiameter)
    return max(left, right)
