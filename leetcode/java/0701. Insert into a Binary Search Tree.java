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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        var node = root;
        var newNode = new TreeNode(val);
        if(root==null) return newNode;
        while(true){
            if(val < node.val){
                if(node.left == null) {
                    node.left = newNode;
                    break;
                }
                node = node.left;
            }
            else {
                if(node.right == null){
                    node.right = newNode;
                    break;
                }
                node = node.right;
            }

        }
        return root;
    }
}