/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// Key Insights
// At any node:
// If one of p or q is found in the left subtree, and the other is in the right, that node is the LCA.
// If current node is p or q, and the other node is found below, current node is LCA.
// If neither p nor q is in the subtree, return null.

// Recursive
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return dfs(root, p, q);
    }

    private TreeNode dfs(TreeNode node, TreeNode p, TreeNode q) {
        // Base case: if we reach the end or find p or q
        if (node == null || node == p || node == q)
            return node;

        TreeNode left = dfs(node.left, p, q);
        TreeNode right = dfs(node.right, p, q);

        // If p and q are found on different sides, current node is LCA
        if (left != null && right != null)
            return node;

        return left != null ? left : right;
    }
}

//Iterative
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        parent.put(root, null);
        stack.push(root);

        // Step 1: Traverse and populate parent map
        while (!parent.containsKey(p) || !parent.containsKey(q)) {
            TreeNode node = stack.pop();
            if (node.left != null) {
                parent.put(node.left, node);
                stack.push(node.left);
            }
            if (node.right != null) {
                parent.put(node.right, node);
                stack.push(node.right);
            }
        }

        // Step 2: Store all ancestors of p
        Set<TreeNode> ancestors = new HashSet<>();
        while (p != null) {
            ancestors.add(p);
            p = parent.get(p);
        }

        // Step 3: The first ancestor of q found in p's ancestor set is the LCA
        while (!ancestors.contains(q))
            q = parent.get(q);

        return q;
    }
}
