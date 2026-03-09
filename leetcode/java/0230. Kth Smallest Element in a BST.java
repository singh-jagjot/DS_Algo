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

//Time Complexity: O(H+k), Space Complexity: O(H)
class Solution {
    int count = 0;
    int res = -1;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return res;
    }

    public void inorder(TreeNode node, int k) {
        // 1. Base case or Early Exit: Stop if we've found our result
        if (node == null || res != -1) return;

        // 2. Traverse Left
        inorder(node.left, k);

        // 3. Process Current Node
        count++;
        if (count == k) {
            res = node.val;
            return; // Found it!
        }

        // 4. Traverse Right (only if res hasn't been found yet)
        inorder(node.right, k);
    }
}