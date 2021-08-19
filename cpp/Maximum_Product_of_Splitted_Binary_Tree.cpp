/*
DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 21.32 % of cpp submissions.
You are here!
Your memory usage beats 16.72 % of cpp submissions.
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
    int maxProduct(TreeNode* root) {
        const int MOD = 1e9 + 7;
        int total = dfs(root);
        int64_t maxp = 0;
        for (const auto &sub: subsum) {
            maxp = max(maxp, (int64_t)(total - sub) * sub);
        }
        return maxp % MOD;
    }

private:
    unordered_set<int> subsum;
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        int s = node -> val + dfs(node -> left) + dfs(node -> right);
        subsum.insert(s);
        return s;
    }
};
