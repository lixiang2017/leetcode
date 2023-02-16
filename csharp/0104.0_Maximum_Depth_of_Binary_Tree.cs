/*
Runtime: 86 ms, faster than 89.37% of C# online submissions for Maximum Depth of Binary Tree.
Memory Usage: 39.6 MB, less than 62.60% of C# online submissions for Maximum Depth of Binary Tree.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int l = MaxDepth(root.left);
        int r = MaxDepth(root.right);
        return 1 + Math.Max(l, r);
    }
}



/*
Runtime: 83 ms, faster than 95.23% of C# online submissions for Maximum Depth of Binary Tree.
Memory Usage: 39.5 MB, less than 62.60% of C# online submissions for Maximum Depth of Binary Tree.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        return root == null ? 0 : 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
    }
}