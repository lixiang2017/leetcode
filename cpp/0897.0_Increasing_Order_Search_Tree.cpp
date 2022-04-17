/*
Runtime: 6 ms, faster than 20.69% of C++ online submissions for Increasing Order Search Tree.
Memory Usage: 7.6 MB, less than 77.99% of C++ online submissions for Increasing Order Search Tree.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* hair = new TreeNode();
    TreeNode* increasingBST(TreeNode* root) {
        TreeNode* cur = hair;
        function<void(TreeNode*)> inorder = [&] (TreeNode* node) -> void {
            if (nullptr == node) return;
            inorder(node->left);
            node->left = nullptr;
            cur->right = node;
            cur = node;
            inorder(node->right);
        };
        inorder(root);
        return hair->right;
    }
};
