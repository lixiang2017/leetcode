/*
Runtime: 45 ms, faster than 68.15% of C++ online submissions for Convert BST to Greater Tree.
Memory Usage: 33.5 MB, less than 62.77% of C++ online submissions for Convert BST to Greater Tree.
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
    int postsum = 0;
    void dfs(TreeNode* node) {
        if (node == nullptr) return;
        dfs(node->right);
        postsum += node->val;
        node->val = postsum;
        dfs(node->left);
    }
    
    TreeNode* convertBST(TreeNode* root) {
        dfs(root);
        return root;
    }
};



/*
Runtime: 45 ms, faster than 68.15% of C++ online submissions for Convert BST to Greater Tree.
Memory Usage: 33.5 MB, less than 19.37% of C++ online submissions for Convert BST to Greater Tree.
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
    TreeNode* convertBST(TreeNode* root) {
        int postsum = 0;
        function<void(TreeNode*)> dfs = [&] (TreeNode* node) -> void {
            if (node == nullptr) return;
            dfs(node->right);
            postsum += node->val;
            node->val = postsum;
            dfs(node->left);
        };
        dfs(root);
        return root;
    }
};


/*
Runtime: 61 ms, faster than 8.77% of C++ online submissions for Convert BST to Greater Tree.
Memory Usage: 33.5 MB, less than 62.76% of C++ online submissions for Convert BST to Greater Tree.
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
    TreeNode* convertBST(TreeNode* root) {
        int postsum = 0;
        vector<TreeNode*> stk;
        TreeNode* node = root;
        while (node != nullptr || !stk.empty()) {
            if (node) {
                stk.push_back(node);
                node = node->right;
            } else {
                node = stk.back();
                stk.pop_back();
                postsum += node->val;
                node->val = postsum;
                node = node->left;
            }
        }
        return root;
    }
};

