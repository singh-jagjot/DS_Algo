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

//Time: O(N), Space: O(N)
class Solution {
    int postIdx;
    Map<Integer, Integer> inorderMap = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // 1. Build a map to find the index of any value in inorder array in O(1)
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }

        // 2. Start from the last element of postorder (the global root)
        postIdx = postorder.length - 1;

        return build(postorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] postorder, int inStart, int inEnd) {
        // Base case: no elements to construct the subtree
        if (inStart > inEnd) return null;

        // 3. The current element at postIdx is the root of the current subtree
        int rootVal = postorder[postIdx--];
        TreeNode root = new TreeNode(rootVal);

        // 4. Find the dividing point in the inorder array
        int pivot = inorderMap.get(rootVal);

        // 5. IMPORTANT: Build the RIGHT subtree first.
        // In postorder (L-R-Root), moving backwards gives (Root-R-L).
        root.right = build(postorder, pivot + 1, inEnd);
        root.left = build(postorder, inStart, pivot - 1);

        return root;
    }
}

//My Solution, Inefficient Time: O(N^2), Space: O(N), Above recommended
class Solution {
    Map<Integer, Integer> inorderIndices = new HashMap<>();
    Map<Integer, Integer> postorderIndices = new HashMap<>();
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        for (int i = 0; i < inorder.length; i++) {
            var inorderVal = inorder[i];
            var postorderVal = postorder[i];
            inorderIndices.put(inorderVal, i);
            postorderIndices.put(postorderVal, i);
        }

        return makeTree(inorder, 0, postorder.length-1);
    }

    TreeNode makeTree(int[] inorder, int i, int j){
        if(i>j) return null;
        TreeNode node = new TreeNode(nextRoot(inorder, i, j));
        node.left = makeTree(inorder, i,inorderIndices.get(node.val)-1);
        node.right = makeTree(inorder, inorderIndices.get(node.val)+1,j);
        return node;
    }

    int nextRoot(int[] inorder, int i, int j){
        int maxIdx = Integer.MIN_VALUE;
        int inorderIdx = Integer.MIN_VALUE;
        for (int k = i; k <= j ; k++) {
            int currMaxIdx = postorderIndices.get(inorder[k]);
            if(currMaxIdx > maxIdx) {
                maxIdx = currMaxIdx;
                inorderIdx = k;
            }
        }
        return inorder[inorderIdx];
    }
}