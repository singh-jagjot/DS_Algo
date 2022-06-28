from typing import List


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootidx: int) -> None:
        self.rootidx = rootidx

# O(n) Time | O(h) space[for recursive call stack]


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
