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


// Inorder, Postorder and Preorder traversals are types of DFS traversals.

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> lst = new ArrayList<>();
        helper(root, lst);
        return lst;
    }
    public void helper(TreeNode node, List<Integer> lst){
        if(node==null) return;
        helper(node.left, lst);
        lst.add(node.val);
        helper(node.right, lst);
    }
}