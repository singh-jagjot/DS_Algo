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
    boolean isBalanced = true;
    public boolean isBalanced(TreeNode root) {
        getHeight(root);
        return isBalanced;
    }

    int getHeight(TreeNode node){
        if(node==null|| !isBalanced) return -1;
        int left = getHeight(node.left) + 1;
        int right = getHeight(node.right) + 1;
        if(Math.abs(left-right) > 1){
            isBalanced = false;
        }
        return Math.max(left, right);
    }
}