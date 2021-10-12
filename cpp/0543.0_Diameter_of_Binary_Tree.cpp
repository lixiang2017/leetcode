/*
DFS

Runtime: 16 ms, faster than 33.05% of C++ online submissions for Diameter of Binary Tree.
Memory Usage: 20.3 MB, less than 26.51% of C++ online submissions for Diameter of Binary Tree.
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
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        height(root, diameter);
        return diameter;
    }
private:
    int height(TreeNode* node, int& diameter) {
        if (!node) {
            return 0;
        }
        int lh = height(node->left, diameter);
        int rh = height(node->right, diameter);
        diameter = max(diameter, lh + rh);
        return 1 + max(lh, rh);
    }
};
