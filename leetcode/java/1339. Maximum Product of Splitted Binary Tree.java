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
    long maxProd = 0;
    long totalSum = 0;

    public int maxProduct(TreeNode root) {
        // Pass 1: Get the total sum of the tree
        totalSum = getTotalSum(root);

        // Pass 2: Calculate subtree sums and update maxProd simultaneously
        findMax(root);

        return (int) (maxProd % 1_000_000_007);
    }

    private long getTotalSum(TreeNode node) {
        if (node == null) return 0;
        return node.val + getTotalSum(node.left) + getTotalSum(node.right);
    }

    private long findMax(TreeNode node) {
        if (node == null) return 0;

        // Post-order: Get the sum of the current subtree
        long currentSubtreeSum = node.val + findMax(node.left) + findMax(node.right);

        // Calculate the product if we cut the edge above this node
        long currentProduct = currentSubtreeSum * (totalSum - currentSubtreeSum);

        // Update the global maximum
        if (currentProduct > maxProd) {
            maxProd = currentProduct;
        }

        return currentSubtreeSum;
    }
}

// Above is recommended as it doesn't change the node values!

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