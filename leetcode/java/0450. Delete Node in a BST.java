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
        public TreeNode deleteNodeRecursive(TreeNode root, int key) {
        if(root==null) return null;
        if(root.val==key){
            if(root.left==null) return root.right;
            else if(root.right==null) return root.left;
            else{
                var node = root.right;
                while(node.left!=null){
                    node=node.left;
                }
                root.val = node.val;
                root.right = deleteNode(root.right, root.val);
            }
        } else if (key < root.val) root.left = deleteNode(root.left, key);
        else root.right = deleteNode(root.right, key);
        return root;
    }

    public TreeNode deleteNodeIterative(TreeNode root, int key) {
        TreeNode current = root;
        TreeNode parent = null;
        while(current!=null && current.val!=key){
            parent = current;
            if(key<current.val){
                current = current.left;
            } else {
                current = current.right;
            }
        }
        if(current==null) return root;
        if(current.left==null && current.right==null){
            if(parent==null) return null;
            if(parent.left==current) parent.left=null;
            else parent.right=null; 
        } else if(current.left==null){
            if(parent==null) return current.right;
            if(parent.left==current) parent.left=current.right;
            else parent.right=current.right;
        } else if(current.right==null){
            if(parent==null) return current.left;
            if(parent.left==current) parent.left=current.left;
            else parent.right=current.left;
        } else{
            TreeNode smallest = current.right;
            while(smallest.left!=null) smallest=smallest.left;
            current.val=smallest.val;
            current.right=deleteNode(current.right, smallest.val);
        }
        return root;
    }

    public TreeNode deleteNode(TreeNode root, int key){
        // return deleteNodeRecursive(root, key);
        return deleteNodeIterative(root, key);
    }
}