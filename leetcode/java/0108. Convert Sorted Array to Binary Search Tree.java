/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */

//Time: O(N), Space: O(N) because we are creating a new tree
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        // Base case: if array is empty
        if (nums == null || nums.length == 0) return null;
        return helper(nums, 0, nums.length - 1);
    }

    private TreeNode helper(int[] nums, int left, int right) {
        // 1. Base Case: If the range is invalid, we've reached a leaf's child
        if (left > right) return null;

        // 2. Choose the middle element as the root to maintain balance.
        // Using (left + right) / 2 is fine, but this prevents integer overflow.
        int mid = left + (right - left) / 2;

        TreeNode node = new TreeNode(nums[mid]);

        // 3. Recursively build the left subtree using the left half of the current range.
        node.left = helper(nums, left, mid - 1);

        // 4. Recursively build the right subtree using the right half of the current range.
        node.right = helper(nums, mid + 1, right);

        return node;
    }
}