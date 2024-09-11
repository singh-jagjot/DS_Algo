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
    int maxDia = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        findMaxDia(root);
        return maxDia;
    }

    public int findMaxDia(TreeNode node){
        if(node==null) return -1;
        int left = findMaxDia(node.left) + 1;
        int right = findMaxDia(node.right) + 1;
        maxDia = Math.max(maxDia, left+right);
        return Math.max(left, right);
    }
}