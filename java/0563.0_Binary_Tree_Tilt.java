/*
BFS, post order
T: O(2N)
S: O(N)

执行用时：6 ms, 在所有 Java 提交中击败了21.89% 的用户
内存消耗：38.7 MB, 在所有 Java 提交中击败了15.16% 的用户
通过测试用例：77 / 77
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
    public int findTilt(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Deque<TreeNode> stk = new LinkedList<>();
        LinkedList<TreeNode> tree = new LinkedList<>();
        stk.push(root);
        while (!stk.isEmpty()) {
            TreeNode node = stk.pop();
            tree.addFirst(node);
            if (node.left != null) {
                stk.push(node.left);
            }
            if (node.right != null) {
                stk.push(node.right);
            }
        }

        int ans = 0;
        for (TreeNode node: tree) {
            int left = node.left == null ? 0 : node.left.val;
            int right = node.right == null ? 0 : node.right.val;
            ans += Math.abs(left - right);
            node.val += left + right;
        }
        return ans;
    }
}
