/*
执行用时：4 ms, 在所有 C++ 提交中击败了91.65% 的用户
内存消耗：7.1 MB, 在所有 C++ 提交中击败了58.46% 的用户
通过测试用例：81 / 81
*/
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int> dp(26);
        int k = 0;
        for (int i = 0; i < p.length(); ++i) {
            if (i && (p[i] - p[i - 1] + 26) % 26 == 1) {
                ++k;
            } else {
                k = 1;
            }
            dp[p[i] - 'a'] = max(dp[p[i] - 'a'], k);
        }
        return accumulate(dp.begin(), dp.end(), 0);
    }
};
