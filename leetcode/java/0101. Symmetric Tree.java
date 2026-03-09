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

//Time: O(N), Space: O(H) where H is height of the tree
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return helper(root.left, root.right);
    }

    public boolean helper(TreeNode left, TreeNode right) {
        if (left == null && right == null)
            return true;
        if (left == null || right == null || left.val != right.val)
            return false;
        return helper(left.left, right.right) && helper(left.right, right.left);
    }
}

//OR

//Time: O(N), Space: O(H) where H is height of the tree
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root==null) return true;
        return isMirror(root.left, root.right);
    }

    public boolean isMirror(TreeNode left, TreeNode right){
        if((left!=null&&right!=null)&&left.val==right.val){
            return isMirror(left.left, right.right) && isMirror(left.right, right.left);
        }
        return left==right;
    }
}
