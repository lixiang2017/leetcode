/*
DFS

执行用时：16 ms, 在所有 C++ 提交中击败了26.95% 的用户
内存消耗：32.8 MB, 在所有 C++ 提交中击败了20.15% 的用户
通过测试用例：115 / 115
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
    vector<vector<int>> ans;
    vector<int> path;

    void dfs(TreeNode* node, int targetSum, int cur_sum, vector<int> path) {
        path.push_back(node->val);
        if (node->left) {
            dfs(node->left, targetSum, cur_sum + node->val, path);
        }
        if (node->right) {
            dfs(node->right, targetSum, cur_sum + node->val, path);
        }
        if (node->left==nullptr && node->right==nullptr && cur_sum + node->val == targetSum) {
            ans.push_back(path);
        }
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        if (nullptr == root) {
            return ans;
        }
        dfs(root, targetSum, 0, path);
        return ans;
    }
};
