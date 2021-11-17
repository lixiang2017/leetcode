/*
执行用时：20 ms, 在所有 C++ 提交中击败了92.92% 的用户
内存消耗：14.4 MB, 在所有 C++ 提交中击败了8.26% 的用户
通过测试用例：86 / 86
*/

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> q;
        for (auto row: matrix) {
            for (auto num: row) {
                q.push(num);
                if (q.size() > k) {
                    q.pop();
                }
            }
        }
        return q.top();
    }
};
