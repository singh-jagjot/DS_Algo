# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, value):
        self.value = value

# O(n) time | O(h) space
def splitBinaryTree(tree):
    # Write your code here.
    treeInfo = TreeInfo(0)
    splitBinaryTree_(tree, treeSum(tree) / 2, treeInfo)
    return treeInfo.value

def treeSum(root):
    if root is None:
        return 0
    return root.value + treeSum(root.left) + treeSum(root.right)

def splitBinaryTree_(root, expectedSum, treeInfo):
    if root is None:
        return 0
    leftSum = splitBinaryTree_(root.left, expectedSum, treeInfo)
    rightSum = splitBinaryTree_(root.right, expectedSum, treeInfo)
    if leftSum == expectedSum or rightSum == expectedSum:
        treeInfo.value = expectedSum
    return root.value + leftSum + rightSum