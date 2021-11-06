/*
执行用时：12 ms, 在所有 C++ 提交中击败了59.20% 的用户
内存消耗：11.2 MB, 在所有 C++ 提交中击败了14.24% 的用户
通过测试用例：69 / 69
*/

class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        for (auto op: ops) {
            m = min(m, op[0]);
            n = min(n, op[1]);
        }
        return m * n;
    }
};



/*
执行用时：8 ms, 在所有 C++ 提交中击败了90.97% 的用户
内存消耗：10.8 MB, 在所有 C++ 提交中击败了59.90% 的用户
通过测试用例：69 / 69
*/
class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        for (int i = 0; i < ops.size(); ++i) {
            m = min(m, ops[i][0]);
            n = min(n, ops[i][1]);
        }
        return m * n;
    }
};

