# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    # Write your code here.
    return helper(tree)

def helper(node):
    if node is None:
        return
    lres = helper(node.left)
    rres = helper(node.right)
    if lres == rres == None:
        return node.value
        
    res = 0
    if node.value == -1:
        res = lres + rres
    elif node.value == -2:
        res = lres - rres
    elif node.value == -3:
        res = int(lres / rres)
    else:
        res = lres * rres

    return res
    