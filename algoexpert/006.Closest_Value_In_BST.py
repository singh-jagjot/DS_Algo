def min_diff(root, key):
    current_closest_diff = abs(key - root.data)
    current_node = root
    while True:
        if key < current_node.data:
            if current_node.left is not None:
                current_node = current_node.left
                diff = abs(key - current_node.data)
                if diff < current_closest_diff:
                    current_closest_diff = diff
            else:
                break
        elif key > current_node.data:
            if current_node.right is not None:
                current_node = current_node.right
                diff = abs(key - current_node.data)
                if diff < current_closest_diff:
                    current_closest_diff = diff
            else:
                return current_closest_diff
        else:
            break
    return current_closest_diff


# Better solution with less code but same complexity
def find_closest_value_in_bst(tree, target):
    current_node = tree
    closest = float('inf')
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest


# Recursive Solution
def find_closest_value_in_bst_recursive(tree, target):
    return find_closest_value_in_bst_helper(tree, target, float("inf"))


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
