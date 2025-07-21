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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> traversal = new ArrayList<>();
        if (root == null) return traversal;

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.offerLast(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> levelVals = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.removeFirst();
                levelVals.add(node.val);
                if (node.left != null) queue.offerLast(node.left);
                if (node.right != null) queue.offerLast(node.right);
            }
            traversal.add(levelVals);
        }

        return traversal;
    }
}

// OR MY FIRST AC SUBMISSION(ABOVE RECOMMENDED)

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> traversal = new ArrayList<>();
        if (root != null) {
            Deque<List<TreeNode>> queue = new ArrayDeque<>();
            List<TreeNode> level = new ArrayList<>();
            level.add(root);
            queue.offerLast(level);

            while (!queue.isEmpty()) {
                List<TreeNode> currentLevel = queue.removeFirst();
                level = new ArrayList<>();
                List<Integer> levelVals = new ArrayList<>();
                for (TreeNode node: currentLevel){
                    levelVals.add(node.val);
                    if(node.left!=null) level.add(node.left);
                    if(node.right!=null) level.add(node.right);
                }
                if(!level.isEmpty()) queue.offerLast(level);
                if(!levelVals.isEmpty()) traversal.add(levelVals);
            }
        }
        return traversal;
    }
}