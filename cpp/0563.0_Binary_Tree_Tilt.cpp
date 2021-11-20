/*
DFS
call by reference
T: O(N)
S: O(N)

执行用时：16 ms, 在所有 C++ 提交中击败了73.23% 的用户
内存消耗：23.5 MB, 在所有 C++ 提交中击败了7.35% 的用户
通过测试用例：77 / 77
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
    int findTilt(TreeNode* root) {
        int sum = 0;
        return sumTilt(root, sum);
    }

    int sumTilt(TreeNode* node, int& sum) {
        if (node == nullptr) {
            return 0;
        }
        int sumL = 0;
        int sumR = 0;
        int tiltL = sumTilt(node->left, sumL);
        int tiltR = sumTilt(node->right, sumR);
        sum = sumL + sumR + node->val;
        return abs(sumL - sumR) + tiltL + tiltR;
    }
};


/*
DFS
T: O(N)
S: O(N)

执行用时：20 ms, 在所有 C++ 提交中击败了49.81% 的用户
内存消耗：23.6 MB, 在所有 C++ 提交中击败了6.85% 的用户
通过测试用例：77 / 77
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
    int findTilt(TreeNode* root) {
        return dfs(root).second;
    }
    // {sum, tilt}
    pair<int, int> dfs(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }
        // left_sum, left_tilt
        auto [ls, lt] = dfs(node->left);
        auto [rs, rt] = dfs(node->right);
        return {ls + rs + node->val, lt + rt + abs(ls - rs)};
    }
};



/*
BFS, post order
T: O(2N)
S: O(N)

执行用时：8 ms, 在所有 C++ 提交中击败了98.38% 的用户
内存消耗：23.8 MB, 在所有 C++ 提交中击败了5.11% 的用户
通过测试用例：77 / 77
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
    int findTilt(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        stack<TreeNode*> stk;
        vector<TreeNode*> tree;
        stk.push(root);
        while (!stk.empty()) {
            TreeNode* node = stk.top();
            stk.pop();
            tree.push_back(node);
            if (node->left != nullptr) {
                stk.push(node->left);
            }
            if (node->right != nullptr) {
                stk.push(node->right);
            }
        }

        int ans = 0;
        for (int i = tree.size() - 1; i >= 0; i--) {
            int left = (tree[i]->left == nullptr) ? 0: tree[i]->left->val;
            int right = (tree[i]->right == nullptr) ? 0: tree[i]->right->val;
            ans += abs(left - right);
            tree[i]->val += left + right;
        }
        return ans;
    }
};




