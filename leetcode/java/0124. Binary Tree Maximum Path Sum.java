/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

// Time: O(n) - We visit each node exactly once.
// Space: O(h) - Where h is the height of the tree, due to the recursion stack.
class Solution {
    private int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        findMaxPath(root);
        return maxSum;
    }

    private int findMaxPath(TreeNode node) {
        if (node == null) return 0;

        // 1. Calculate max gain from left and right subtrees.
        // IMPORTANT: If a subtree sum is negative, we discard it by taking Math.max(0, ...)
        int leftGain = Math.max(0, findMaxPath(node.left));
        int rightGain = Math.max(0, findMaxPath(node.right));

        // 2. The price of the path with the current node as the highest "peak".
        // This connects the left branch, the current node, and the right branch.
        int currentPathSum = node.val + leftGain + rightGain;

        // 3. Update the global maximum if the new path is better.
        maxSum = Math.max(maxSum, currentPathSum);

        // 4. Return the maximum "branch" sum to the parent.
        // A parent can only use ONE branch (left or right) to maintain a valid path.
        return node.val + Math.max(leftGain, rightGain);
    }
}

//My Sol
//Time: O(n), Space: O(h)
class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        findMaxPath(root);
        return maxSum;
    }

    int findMaxPath(TreeNode node) {
        if (node == null) return 0;

        int rightSum = findMaxPath(node.right);
        int leftSum = findMaxPath(node.left);
        int pathSum = node.val + rightSum + leftSum;
        if(maxSum < pathSum) maxSum = pathSum;
        int maxBranchSum = Math.max(rightSum, leftSum);
        return Math.max(0, node.val+maxBranchSum);
    }
}