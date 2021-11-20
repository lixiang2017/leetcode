/*
DFS

执行用时：12 ms, 在所有 C++ 提交中击败了94.33% 的用户
内存消耗：10.4 MB, 在所有 C++ 提交中击败了93.79% 的用户
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
    int maxDepth(Node* root) {
        if (root == nullptr) {
            return 0;
        }
        int max_child_depth = 0;
        for (auto child: root->children) {
            max_child_depth = max(max_child_depth, maxDepth(child));
        }
        return max_child_depth + 1;
    }
};
