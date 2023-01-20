/*
hash table

执行用时：204 ms, 在所有 C++ 提交中击败了85.48% 的用户
内存消耗：83.4 MB, 在所有 C++ 提交中击败了55.64% 的用户
通过测试用例：38 / 38
*/
class Solution {
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        unordered_map<int, unordered_set<int>> id2times;
        for (auto &log: logs) {
            id2times[log[0]].insert(log[1]);
        }
        vector<int> ans(k);
        for (auto &it: id2times) {
            ans[it.second.size() - 1]++;
        }
        return ans;
    }
};
