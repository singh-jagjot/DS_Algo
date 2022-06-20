from typing import Any


class BST:
    def __init__(self, value) -> None:
        self.value: Any = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    # Here we added 'parent' parameter to remove the currentNode if it doesn't have either of left or right child.

    def remove(self, value, parent=None):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                # This case is for a root node where it doesn't have either of left or right child.
                elif parent is None:
                    # Here value of current_node.left and current_node.right is not 'None' because not
                    # either child of root node can have further children.
                    if current_node.left is not None:
                        # Beware of the order here or else we can get null pointer exception
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        current_node.value = None
                elif parent.left == current_node:
                    parent.left = current_node.left if current_node.right is None else current_node.right
                elif parent.right is current_node:
                    parent.right = current_node.left if current_node.right is None else current_node.right
                break
        return self
