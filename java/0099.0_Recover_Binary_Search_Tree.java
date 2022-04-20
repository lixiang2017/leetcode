/*
iteration for inorder

Runtime: 6 ms, faster than 14.05% of Java online submissions for Recover Binary Search Tree.
Memory Usage: 46.9 MB, less than 69.94% of Java online submissions for Recover Binary Search Tree.
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
    public void recoverTree(TreeNode root) {
        TreeNode prev = null;
        TreeNode first = null;
        TreeNode second = null;
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<>();
        while (node != null || !stack.isEmpty()) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                if (first == null && prev != null && prev.val > node.val) {
                    first = prev;
                }
                if (first != null && prev != null && prev.val > node.val) {
                    second = node;
                }
                prev = node;
                node = node.right;
            }
        }
        // swap
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}
