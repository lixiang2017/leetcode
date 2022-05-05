/*
in place

执行用时：16 ms, 在所有 C++ 提交中击败了18.84% 的用户
内存消耗：9.4 MB, 在所有 C++ 提交中击败了70.49% 的用户
通过测试用例：29 / 29
*/
class Solution {
public:
    string reverseWords(string s) {
        int i = 0, n = s.length();
        while (i < n) {
            int start = i;
            while (i < n && s[i] != ' ') {
                i++;
            }
            int l = start, r = i - 1;
            while (l < r) {
                swap(s[l++], s[r--]);
            }
            while (i < n && s[i] == ' ') {
                i++;
            }
        }
        return s;
    }
};
