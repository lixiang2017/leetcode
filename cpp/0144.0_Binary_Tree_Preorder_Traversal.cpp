/*
iteration, if

执行用时：4 ms, 在所有 C++ 提交中击败了40.34% 的用户
内存消耗：8.1 MB, 在所有 C++ 提交中击败了75.85% 的用户
通过测试用例：69 / 69
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        TreeNode* node = root;
        while(node != nullptr || !s.empty()) {
            if (node != nullptr) {
                ans.push_back(node->val);
                s.push(node);
                node = node->left;
            } else {
                node = s.top();
                s.pop();
                node = node->right;
            }
        }
        return ans;
    }
};


/*
iteration, while

执行用时：4 ms, 在所有 C++ 提交中击败了40.34% 的用户
内存消耗：8.2 MB, 在所有 C++ 提交中击败了37.55% 的用户
通过测试用例：69 / 69
*/
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        TreeNode* node = root;
        while(node != nullptr || !s.empty()) {
            while (node != nullptr) {
                ans.push_back(node->val);
                s.push(node);
                node = node->left;
            }
            node = s.top();
            s.pop();
            node = node->right;
        }
        return ans;
    }
};


/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了13.50% 的用户
通过测试用例：69 / 69
*/
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        TreeNode* node = nullptr;
        if (root != nullptr) {
            s.push(root);
        }
        while (!s.empty()) {
            node = s.top();
            s.pop();
            ans.push_back(node->val);
            if (node->right != nullptr) {
                s.push(node->right);
            }
            if (node->left != nullptr) {
                s.push(node->left);
            }
        }
        return ans;
    }
};



