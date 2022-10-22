from typing import List


def inorderTraversal(root) -> List[int]:
    lst = []

    def helper(root, lst):
        if not root:
            return
        helper(root.left, lst)
        lst.append(root.val)
        helper(root.right, lst)
    helper(root, lst)
    return lst


def preorderTraversal(root) -> List[int]:
    lst = []

    def helper(root, lst):
        if not root:
            return
        lst.append(root.val)
        helper(root.left, lst)
        helper(root.right, lst)
    helper(root, lst)
    return lst


def postorderTraversal(root) -> List[int]:
    lst = []

    def helper(root, lst):
        if not root:
            return
        helper(root.left, lst)
        helper(root.right, lst)
        lst.append(root.val)
    helper(root, lst)
    return lst


# Better algorithm exits 'Morris in-order traversal' for tree traversal without recursion and stack(iterative)