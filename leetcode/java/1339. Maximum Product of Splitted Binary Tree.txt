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
    long product = 0;
    long sum = 0;
    long mod = 1000_000_007;

    public int maxProduct(TreeNode root) {
        sum = getSumInplace(root);
        calMaxProduct(root);
        return (int) (product % mod);
    }

    int getSumInplace(TreeNode node) {
        if (node == null)
            return 0;
        node.val = node.val + getSumInplace(node.left) + getSumInplace(node.right);
        return node.val;
    }

    // void calMaxProduct(TreeNode node){
    //     if(node==null) return;
    //     long leftProd=0,rightProd=0;
    //     if(node.left!=null) leftProd = (sum - node.left.val) * node.left.val;
    //     if(node.right!=null) rightProd = (sum - node.right.val) * node.right.val;
    //     product = Math.max(product, Math.max(leftProd, rightProd));
    //     calMaxProduct(node.left);
    //     calMaxProduct(node.right);
    // }

    void calMaxProduct(TreeNode node) {
        if (node == null)
            return;
        product = Math.max(product, (sum - node.val) * node.val);
        calMaxProduct(node.left);
        calMaxProduct(node.right);
    }
}