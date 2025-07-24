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
class Solution {
    int currMaxDepth = 0;
    TreeNode lca = null;

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        dfs(root, 0);
        return lca;
    }

    public int dfs(TreeNode node, int depth) {
        if (node == null) {
            if (depth > currMaxDepth) currMaxDepth = depth;
            return depth;
        }
        int left = dfs(node.left, depth + 1);
        int right = dfs(node.right, depth + 1);
        if (left == right && left == currMaxDepth) lca = node;
        return Math.max(left, right);
    }
}