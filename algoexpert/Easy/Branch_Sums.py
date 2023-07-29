# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space
def branchSums(root):
    # Write your code here.
    lst = []
    helper(root, 0, lst)
    return lst

def helper(node, sum, lst):
    if node is None :
        return
    
    sum += node.value
    if node.left is None and node.right is None:
        lst.append(sum)
    else:
        helper(node.left, sum, lst)
        helper(node.right, sum, lst)
    