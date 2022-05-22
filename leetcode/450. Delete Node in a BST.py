# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinRight(self, node):
        currentNode = node
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int, parent = None) -> Optional[TreeNode]:
        currentNode = root
        while currentNode is not None:
            if key < currentNode.val:
                parent = currentNode
                currentNode = currentNode.left
            elif key > currentNode.val:
                parent = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.val = self.getMinRight(currentNode.right)
                    self.deleteNode(currentNode.right, currentNode.val, currentNode)
                elif parent == None:
                    if currentNode.left is not None:
                        currentNode.val = currentNode.left.val
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.val = currentNode.right.val
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        return
                elif parent.left == currentNode:
                    parent.left = currentNode.right if currentNode.left is None else currentNode.left
                elif parent.right == currentNode:
                    parent.right = currentNode.right if currentNode.left is None else currentNode.left
                break
        return root