# O(n) time| O(h) space
def invertBinaryTree(tree):
    # Write your code here.
    return invertBinaryTree_(tree)

def invertBinaryTree_(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    invertBinaryTree_(node.left)
    invertBinaryTree_(node.right)
    return node

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
