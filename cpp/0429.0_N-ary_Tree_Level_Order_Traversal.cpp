/*
BFS

执行用时：16 ms, 在所有 C++ 提交中击败了79.75% 的用户
内存消耗：11.7 MB, 在所有 C++ 提交中击败了18.26% 的用户
通过测试用例：38 / 38
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        if (!root) return ans;
        queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            int n = q.size();
            vector<int> level;
            while (n--) {
                Node *p = q.front();
                q.pop();
                level.push_back(p->val);
                for (int i=0; i < p->children.size(); i++) {
                    q.push(p->children[i]);
                }
            }
            ans.push_back(level);
        }
        return ans;
    }
};





/*
BFS

执行用时：12 ms, 在所有 C++ 提交中击败了97.03% 的用户
内存消耗：11.5 MB, 在所有 C++ 提交中击败了84.51% 的用户
通过测试用例：38 / 38
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (nullptr == root) return {};
        queue<Node*> q;
        vector<vector<int>> ans;
        q.push(root);
        while (!q.empty()) {
            int n = q.size();
            vector<int> level;
            for (int i = 0; i < n; i++) {
                Node *p = q.front();
                q.pop();
                level.push_back(p->val);
                for (auto ch: p->children) {
                    q.push(ch);
                }
            }
            ans.push_back(level);
        }
        return ans;
    }
};


/*
执行用时：12 ms, 在所有 C++ 提交中击败了97.03% 的用户
内存消耗：11.5 MB, 在所有 C++ 提交中击败了80.82% 的用户
通过测试用例：38 / 38
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (nullptr == root) return {};
        queue<Node*> q;
        vector<vector<int>> ans;
        q.push(root);
        while (!q.empty()) {
            int n = q.size();
            ans.push_back(vector<int>());
            for (int i = 0; i < n; i++) {
                Node *p = q.front();
                q.pop();
                ans.back().push_back(p->val);
                for (auto& ch: p->children) {
                    q.push(ch);
                }
            }
        }
        return ans;
    }
};



