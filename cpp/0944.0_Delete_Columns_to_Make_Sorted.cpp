/*
执行用时：36 ms, 在所有 C++ 提交中击败了68.31% 的用户
内存消耗：11.9 MB, 在所有 C++ 提交中击败了42.44% 的用户
通过测试用例：85 / 85
*/
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int ans = 0;
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 0; j < strs.size() - 1; ++j) {
                if (strs[j][i] > strs[j + 1][i]) {
                    ++ans;
                    break;
                }
            }
        }
        return ans;
    }
};
