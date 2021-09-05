/*
执行用时：8 ms, 在所有 C++ 提交中击败了21.90% 的用户
内存消耗：10.3 MB, 在所有 C++ 提交中击败了70.80% 的用户
通过测试用例：106 / 106
*/

class Solution {
public:
    string orderlyQueue(string s, int k) {
        if (k > 1) {
            sort(s.begin(), s.end());
            return s;
        }
        string ans = s;
        for (int i = 1; i < s.length(); i++) {
            ans = min(ans, s.substr(i) + s.substr(0, i));
        }
        return ans;
    }
};
