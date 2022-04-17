/*
Runtime: 0 ms, faster than 100.00% of C online submissions for Increasing Order Search Tree.
Memory Usage: 6.3 MB, less than 20.00% of C online submissions for Increasing Order Search Tree.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

typedef struct TreeNode TreeNode;
TreeNode* cur = NULL;
TreeNode* increasingBST(TreeNode* root){
    TreeNode* hair = (TreeNode*) malloc(sizeof(TreeNode));
    cur = hair;
    inorder(root);
    return hair->right;
}

void inorder(TreeNode* node) {
    if (node == NULL) return;
    inorder(node->left);
    node->left = NULL;
    cur->right = node;
    cur = node;
    inorder(node->right);
}
