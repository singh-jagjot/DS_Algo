from typing import List

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

# O(n) Time | O(h) space[for recursive call stack]


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootidx: int) -> None:
        self.rootidx = rootidx


def reconstruct_bst(pre_odr_vals: List):
    treeinfo = TreeInfo(0)

    def bst_from_range(lowerbound, upperbound, pre_odr_vals: List, currentsubtreeinfo: TreeInfo):
        if currentsubtreeinfo.rootidx == len(pre_odr_vals):
            return None
        rootvalue = pre_odr_vals[currentsubtreeinfo.rootidx]
        if rootvalue <= lowerbound or rootvalue >= upperbound:
            return None

        currentsubtreeinfo.rootidx += 1
        leftsubtree = bst_from_range(
            lowerbound, rootvalue, pre_odr_vals, currentsubtreeinfo)
        rightsubtree = bst_from_range(
            rootvalue, upperbound, pre_odr_vals, currentsubtreeinfo)
        return Node(rootvalue, leftsubtree, rightsubtree)

    return bst_from_range(float("-inf"), float("inf"), pre_odr_vals, treeinfo)
