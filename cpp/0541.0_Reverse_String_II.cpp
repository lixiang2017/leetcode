/*
执行用时：4 ms, 在所有 C++ 提交中击败了85.41% 的用户
内存消耗：7.2 MB, 在所有 C++ 提交中击败了41.52% 的用户
*/
class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.length();
        for (int i = 0; i < n; i += 2 * k) {
            reverse(s.begin() + i, s.begin() + min(i + k, n));
        }
        return s;
    }
};
