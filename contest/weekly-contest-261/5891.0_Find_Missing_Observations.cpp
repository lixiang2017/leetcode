/*
执行用时：124 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：111 MB, 在所有 C++ 提交中击败了100.00% 的用户
通过测试用例：64 / 64
*/

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int nsum = mean * (rolls.size() + n) - accumulate(rolls.begin(), rolls.end(), 0);
        if (nsum > 6 * n || nsum < n) {
            return {};
        }
        vector<int> ans(n, nsum / n);
        for (int i = 0; i < nsum % n; ++i) {
            ans[i]++;
        }
        return ans;
    }
};
