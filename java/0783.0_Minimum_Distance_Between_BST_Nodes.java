/*
DFS

Runtime: 0 ms, faster than 100.00% of Java online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 40 MB, less than 58.93% of Java online submissions for Minimum Distance Between BST Nodes.
*/
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
    int minDistance = Integer.MAX_VALUE;
    TreeNode prevValue;
    
    void inorderTraversal(TreeNode root) {
        if (root == null) {
            return;
        }
        inorderTraversal(root.left);
        if (prevValue != null) {
            minDistance = Math.min(minDistance, root.val - prevValue.val);
        }
        prevValue = root;
        inorderTraversal(root.right);
    }
        
    public int minDiffInBST(TreeNode root) {
        inorderTraversal(root);
        return minDistance;
    }
}
