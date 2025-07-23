/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

✅ Logic Review:
You're walking down the tree:
If both nodes are less than current node → go left
If both are greater → go right
If they diverge → this is the lowest common ancestor

✅ This works because in a BST, for any node N:
All nodes in the left subtree < N
All nodes in the right subtree > N
This means:
First split in the path from root to p and from root to q is the LCA.

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode lca = root;
        while((p.val < lca.val && q.val < lca.val) || (p.val > lca.val && q.val> lca.val)) {
            if(p.val < lca.val) lca = lca.left;
            else lca = lca.right;
        }
        return lca;
    }
}