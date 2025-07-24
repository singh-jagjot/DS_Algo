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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if(root1==null) return root2;
        if(root2==null) return root1;
        TreeNode root = new TreeNode(root1.val+root2.val);
        root.left = mergeTrees(root1.left, root2.left);
        root.right = mergeTrees(root1.right, root2.right);
        return root;
    }
}


//Iterative

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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if(root1==null) return root2;
        Deque<TreeNode> stack1 = new LinkedList<>(); //Can't use ArrayDeque here as they don't allow null;
        Deque<TreeNode> stack2 = new LinkedList<>(); //Can't use ArrayDeque here as they don't allow null;

        stack1.push(root1);
        stack2.push(root2);

        while (!stack1.isEmpty()) {

            var node1 = stack1.pop();
            var node2 = stack2.pop();

            if (node2 == null)
                continue;

            node1.val = node1.val + node2.val;
            if (node1.left == null) {
                node1.left = node2.left;
            } else {
                stack1.push(node1.left);
                stack2.push(node2.left);
            }

            if (node1.right == null) {
                node1.right = node2.right;
            } else {
                stack1.push(node1.right);
                stack2.push(node2.right);
            }

        }

        return root1;
    }
}