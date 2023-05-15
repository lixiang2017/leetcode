/*
执行用时：156 ms, 在所有 C++ 提交中击败了71.37% 的用户
内存消耗：64.5 MB, 在所有 C++ 提交中击败了81.94% 的用户
通过测试用例：89 / 89
*/
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        unordered_map<string, int> mp;
        for (int i = 0; i < m; i++) {
            string s = string(n, '0');
            for (int j = 0; j < n; j++) {
                s[j] = '0' + (matrix[i][j] ^ matrix[i][0]);
            }
            mp[s]++;
        }
        int ans = 0;
        for (auto &[k, v] : mp) {
            ans = max(ans, v);
        }
        return ans;
    }
};
