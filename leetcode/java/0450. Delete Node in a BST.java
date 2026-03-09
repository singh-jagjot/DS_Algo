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
//Time Complexity: O(H), Space Complexity: O(H)
// Recursive
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        // 1. Search for the node to delete
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            // 2. Node found! Handle the 3 cases:

            // Case 1 & 2: No child or only one child
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            // Case 3: Two children
            // Find the "Inorder Successor" (smallest value in the right subtree)
            TreeNode successor = findMin(root.right);
            // Replace current node's value with successor's value
            root.val = successor.val;
            // Delete the successor node from the right subtree
            root.right = deleteNode(root.right, successor.val);
        }
        return root;
    }

    private TreeNode findMin(TreeNode node) {
        while (node.left != null) node = node.left;
        return node;
    }
}

//Time Complexity: O(H), Space Complexity: O(1)
// Iterative
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode curr = root;
        TreeNode parent = null;

        // 1. Locate the node and its parent
        while (curr != null && curr.val != key) {
            parent = curr;
            if (key < curr.val) curr = curr.left;
            else curr = curr.right;
        }

        if (curr == null) return root; // Key not found

        // 2. Handle deletion based on the number of children
        if (curr.left != null && curr.right != null) {
            // Case: Two children
            // Find successor and its parent
            TreeNode successor = curr.right;
            TreeNode successorParent = curr;
            while (successor.left != null) {
                successorParent = successor;
                successor = successor.left;
            }
            // Swap value
            curr.val = successor.val;
            // Now 'curr' becomes the 'successor' so we can delete it as a 0/1 child case
            curr = successor;
            parent = successorParent;
        }

        // 3. Delete node with 0 or 1 child
        TreeNode child = (curr.left != null) ? curr.left : curr.right;

        if (parent == null) return child; // Deleting the root

        if (parent.left == curr) parent.left = child;
        else parent.right = child;

        return root;
    }
}