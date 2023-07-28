# Recursive

def nodeDepths(root):
    return helper(root, 0)
    
def helper(node, depth):
    if node is None:
        return 0
    return helper(node.left, depth + 1) + helper(node.right, depth + 1) + depth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



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
