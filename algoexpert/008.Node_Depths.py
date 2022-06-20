class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


# Recursive

def node_depths1(node, depth=0) -> int:
    if node is None:
        return 0
    return depth + node_depths1(node.left, depth + 1) + node_depths1(node.right, depth + 1)


# Iterative

def node_depth2(root) -> int:
    node_stack = [{"node": root, "depth": 0}]
    depth_sum = 0
    while len(node_stack) > 0:
        node_info = node_stack.pop()
        node, depth = node_info["node"], node_info["depth"]
        if node is None:
            continue

        depth_sum += depth
        node_stack.append({"node": node.left, "depth": depth + 1})
        node_stack.append({"node": node.right, "depth": depth + 1})
    return depth_sum
