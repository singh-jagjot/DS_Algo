from typing import List


# O(n) Time | O(h) space[for recursive call stack]
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx) -> None:
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(preOrderTraversalValues, float('-inf'), float('inf'), treeInfo)


def reconstructBstFromRange(preOrderTraversalValues, lowerBound, upperBound, currentTreeInfo):
    if currentTreeInfo.rootIdx == len(preOrderTraversalValues):
        return
    
    nodeValue = preOrderTraversalValues[currentTreeInfo.rootIdx]
    if nodeValue < lowerBound or nodeValue >= upperBound:
        return None
    
    currentTreeInfo.rootIdx += 1

    leftNode = reconstructBstFromRange(preOrderTraversalValues, lowerBound, nodeValue, currentTreeInfo)
    rightNode = reconstructBstFromRange(preOrderTraversalValues, nodeValue, upperBound, currentTreeInfo)
    return BST(nodeValue, leftNode, rightNode)

# O(nlogn) Time | O(1) Space
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_from_preorder(preorder: List[int]):
    root = TreeNode(val=preorder[0])

    def insert(root, val):
        current_node = root
        while True:
            if val < current_node.val:
                if current_node.left is None:
                    current_node.left = TreeNode(val=val)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = TreeNode(val=val)
                    break
                else:
                    current_node = current_node.right

    for x in preorder[1:]:
        insert(root, x)

    return root
