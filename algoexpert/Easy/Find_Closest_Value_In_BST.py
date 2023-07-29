# O(n) time (O(log(n)) in average) | O(1) space
def findClosestValueInBst(tree, target):
    # Write your code here.
    val = float('inf')
    root = tree
    while root is not None:
        val = root.value if abs(target - root.value) < abs(target - val) else val
        if target < root.value:
            root = root.left
        elif target > root.value:
            root = root.right
        else:
            return target
    return val
            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive Solution
# O(n) time (O(log(n)) in average) | O(n) space (O(log(n)) in average) 
def find_closest_value_in_bst_recursive(tree, target):
    return find_closest_value_in_bst_helper(tree, target, tree.value)


def find_closest_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)
    else:
        return closest
