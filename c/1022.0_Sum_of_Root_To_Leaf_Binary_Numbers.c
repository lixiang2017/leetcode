/*
执行用时：4 ms, 在所有 C 提交中击败了85.71% 的用户
内存消耗：6.6 MB, 在所有 C 提交中击败了95.00% 的用户
通过测试用例：63 / 63
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int sumRootToLeaf(struct TreeNode* root){
    return root ? _sumRootToLeaf(root, 0) : 0;
}

int _sumRootToLeaf(struct TreeNode *node, int cur) {
    int s = 0;
    cur = (cur << 1) + node->val;
    if (node->left == NULL && node->right == NULL) return cur;
    if (node->left) s += _sumRootToLeaf(node->left, cur);
    if (node->right) s += _sumRootToLeaf(node->right, cur);
    return s;
}
