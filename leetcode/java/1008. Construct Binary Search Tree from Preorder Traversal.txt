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
    int rootIdx = 0;
    int[] preorder;
    public TreeNode bstFromPreorder(int[] preorder) {
        this.preorder = preorder;
        return createTree(Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    TreeNode createTree(int lower, int upper){
        if(rootIdx == preorder.length) return null;
        int val = preorder[rootIdx];
        TreeNode root = null;
        if(val > lower && val < upper){
            rootIdx++;
            root = new TreeNode(val, createTree(lower, val), createTree(val, upper));
        }
        return root;
    }
}