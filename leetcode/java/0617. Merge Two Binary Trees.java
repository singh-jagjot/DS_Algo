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

//Time Complexity: O(M)
//Here, M is the number of overlapping nodes between the two trees.
//Space Complexity: O(H)
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        // 1. If one node is null, return the other (covers all base cases)
        if (root1 == null) return root2;
        if (root2 == null) return root1;

        // 2. Instead of 'new', reuse root1 to save memory (In-place)
        root1.val += root2.val;

        // 3. Recursively merge children
        root1.left = mergeTrees(root1.left, root2.left);
        root1.right = mergeTrees(root1.right, root2.right);

        // 4. Return the modified root1
        return root1;
    }
}

//Time Complexity: O(M)
//Here, M is the number of overlapping nodes between the two trees.
//Space Complexity: O(H)
//Iterative using DFS
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root1 == null) return root2;
        if (root2 == null) return root1;

        // Now we can use ArrayDeque because we won't push nulls!(ArrayDeque don't allow null)
        Deque<TreeNode> s1 = new ArrayDeque<>();
        Deque<TreeNode> s2 = new ArrayDeque<>();

        s1.push(root1);
        s2.push(root2);

        while (!s1.isEmpty()) {
            TreeNode n1 = s1.pop();
            TreeNode n2 = s2.pop();

            // Merge values
            n1.val += n2.val;

            // Handle Left
            if (n1.left == null) {
                n1.left = n2.left; // Grafting
            } else if (n2.left != null) {
                // Only push if BOTH are non-null
                s1.push(n1.left);
                s2.push(n2.left);
            }

            // Handle Right
            if (n1.right == null) {
                n1.right = n2.right; // Grafting
            } else if (n2.right != null) {
                // Only push if BOTH are non-null
                s1.push(n1.right);
                s2.push(n2.right);
            }
        }
        return root1;
    }
}