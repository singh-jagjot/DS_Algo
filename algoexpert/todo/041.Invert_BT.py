# O(n) time | O(n) space
def invert_bt(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


# O(n) time | O(d) space
def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
