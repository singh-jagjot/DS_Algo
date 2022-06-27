from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> TreeNode:
    def helper(nums, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        left =  helper(nums, start, mid - 1)
        right = helper(nums, mid+1, end)
        node = TreeNode(nums[mid], left=left, right=right)
        return node
    return helper(nums, 0, len(nums) - 1)