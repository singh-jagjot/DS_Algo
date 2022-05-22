class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node = None
        self.right: Node = None

# Rcursive


def nodeDepths1(node, depth=0) -> int:
    if node is None:
        return 0
    return depth + nodeDepths1(node.left, depth+1) + nodeDepths1(node.right, depth+1)

# Iterative


def nodeDepth2(root) -> int:
    nodeStack = [{"node": root, "depth": 0}]
    depthSum = 0
    while len(nodeStack) > 0:
        nodeInfo = nodeStack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue

        depthSum += depth
        nodeStack.append({"node": node.left, "depth": depth+1})
        nodeStack.append({"node": node.right, "depth": depth+1})
    return depthSum
