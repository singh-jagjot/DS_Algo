# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:       
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val = preorder[0])
        def insert(root, val):
            current_node = root
            while True:
                if val < current_node.val:
                    if current_node.left is None:
                        current_node.left = TreeNode(val = val)
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = TreeNode(val = val)
                        break
                    else:
                        current_node = current_node.right
        
        for x in preorder[1:]:
            insert(root, x)
        
        return root
                
                