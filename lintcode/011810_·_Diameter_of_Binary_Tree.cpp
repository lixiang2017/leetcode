/*
Accepted
100%
41 mstime cost
5.47 MBmemory cost
Your submission beats74.00 %Submissions
*/
/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: a root of binary tree
     * @return: return a integer
     */
    int ans = 0;
    int diameterOfBinaryTree(TreeNode *root) {
        // write your code here
        longestBranch(root);
        return ans;
    }

    int longestBranch(TreeNode *node) {
        if (node == nullptr) return 0;
        // left longest 
        int l = longestBranch(node->left);
        // right longest 
        int r = longestBranch(node->right);
        ans = max(ans, l + r);
        return max(l, r) + 1;
    }
};


