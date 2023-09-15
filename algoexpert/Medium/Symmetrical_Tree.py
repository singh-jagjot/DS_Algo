# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h)
# Iterative
def symmetricalTree(tree):
    # Write your code here.
    stackLeft  = [tree.left]
    stackRight = [tree.right]
    while len(stackLeft) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()
        if left is None and right is None:
            continue
        elif left is not None and right is not None and left.value == right.value:
            stackLeft.append(left.left)
            stackLeft.append(left.right)
            stackRight.append(right.right)
            stackRight.append(right.left)
        else:
            return False
    return True

# O(n) time | O(h)
# Recursive
def symmetricalTree(tree):
    return symmetricalTree_(tree.left, tree.right)

def symmetricalTree_(left, right):
    if left is not None and right is not None and left.value == right.value:
        return symmetricalTree_(left.left, right.right) and symmetricalTree_(left.right, right.left)
    return left == right