/*
Runtime: 0 ms, faster than 100.00% of C online submissions for Increasing Order Search Tree.
Memory Usage: 6 MB, less than 71.11% of C online submissions for Increasing Order Search Tree.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* cur = NULL;
struct TreeNode* increasingBST(struct TreeNode* root){
    struct TreeNode* hair = (struct TreeNode*) malloc(sizeof(struct TreeNode));
    cur = hair;
    inorder(root);
    return hair->right;
}

void inorder(struct TreeNode* node) {
    if (node == NULL) return;
    inorder(node->left);
    node->left = NULL;
    cur->right = node;
    cur = node;
    inorder(node->right);
}
