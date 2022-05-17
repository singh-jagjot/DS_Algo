from typing import Any


class BST:
    def __init__(self, value) -> None:
        self.value: Any = value
        self.left: BST = None
        self.right: BST = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value


# Here we added 'parent' parameter to remove the currentNode if it donesn't have either of left or right child.

    def remove(self, value, parent=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parent = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parent = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                # This case is for a root node where it doesn't have either of left or right child.
                elif parent is None:
                    # Here value of currentNode.left and currentNode.right is not 'None' because not
                    # 'None' child of root node can have further children.
                    if currentNode.left is not None:
                        #Beaware of the order here or we can get null pointer exception
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parent.left == currentNode:
                    parent.left = currentNode.left if currentNode.right is None else currentNode.right
                elif parent.right is currentNode:
                    parent.right = currentNode.left if currentNode.right is None else currentNode.right
                break
        return self
