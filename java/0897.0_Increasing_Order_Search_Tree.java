/*
T: O(N)
S: O(H), for recursion stack

Runtime: 0 ms, faster than 100.00% of Java online submissions for Increasing Order Search Tree.
Memory Usage: 40 MB, less than 84.76% of Java online submissions for Increasing Order Search Tree.
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
    TreeNode cur;
    public TreeNode increasingBST(TreeNode root) {
        TreeNode hair = new TreeNode(0);
        cur = hair;
        inorder(root);
        return hair.right;
    }
    
    public void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        node.left = null;
        cur.right = node;
        cur = node;
        inorder(node.right);
    }
}


/*
Runtime: 0 ms, faster than 100.00% of Java online submissions for Increasing Order Search Tree.
Memory Usage: 39.8 MB, less than 88.54% of Java online submissions for Increasing Order Search Tree.
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
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> nums = new ArrayList();
        inorder(root, nums);
        TreeNode hair = new TreeNode(0), cur = hair;
        for (var x: nums) {
            cur.right = new TreeNode(x);
            cur = cur.right;
        }
        return hair.right;
    }
    
    public void inorder(TreeNode node, List<Integer> nums) {
        if (node == null) return;
        inorder(node.left, nums);
        nums.add(node.val);
        inorder(node.right, nums);
    }
}

