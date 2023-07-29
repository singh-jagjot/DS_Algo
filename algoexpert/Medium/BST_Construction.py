# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # O(n) time (O(log(n) on average) | O(1) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
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
    
    # O(n) time (O(log(n) on average) | O(1) space
    def contains(self, value):
        # Write your code here.
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    # O(n) time (O(log(n) on average) | O(1) space
    def remove(self, value, parent = None):
        # Write your code here.
        # Do not edit the return statement of this method.
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
                    # Here value of current_node.left or current_node.right is not 'None' because
                    # they can have further children.
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
                        # Requirement of the Algoexpert solution
                        pass
                        # This will delete the BST
                        # current_node.value = None
                elif parent.left == current_node:
                    parent.left = current_node.left if current_node.right is None else current_node.right
                elif parent.right == current_node:
                    parent.right = current_node.left if current_node.right is None else current_node.right
                break

        return self

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value