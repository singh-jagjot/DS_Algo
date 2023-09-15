# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space, h is height of the shotter tree
def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1
    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    return tree1
