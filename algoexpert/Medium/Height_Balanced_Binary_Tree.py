# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

# O(n) time | O(n) space
def heightBalancedBinaryTree(tree):
    # Write your code here.
    return heightBalancedBinaryTree_(tree).isBalanced


def heightBalancedBinaryTree_(node):
    if node is None:
        return TreeInfo(True, -1)
    leftTreeInfo = heightBalancedBinaryTree_(node.left)
    righTreeInfo = heightBalancedBinaryTree_(node.right)
    isBalanced = False
    height = max(leftTreeInfo.height, righTreeInfo.height) + 1
    if abs(leftTreeInfo.height - righTreeInfo.height) <= 1 and leftTreeInfo.isBalanced and righTreeInfo.isBalanced:
        isBalanced = True
    return TreeInfo(isBalanced, height)
