def minHeightBst(array):
    return helper(array, 0, len(array) - 1)


def helper(array, start, end):
    if start > end:
        return
    mid = (start+end)//2
    left = helper(array, start, mid - 1)
    right = helper(array, mid + 1, end)
    node = BST(array[mid])
    node.left = left
    node.right = right
    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
