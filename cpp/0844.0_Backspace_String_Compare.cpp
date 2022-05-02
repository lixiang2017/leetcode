/*
执行用时：4 ms, 在所有 C++ 提交中击败了9.73% 的用户
内存消耗：6 MB, 在所有 C++ 提交中击败了90.24% 的用户
通过测试用例：114 / 114
*/
class Solution {
private:
    void jump(const string &s, int &i, int &skip) {
        while (i >= 0) {
            if (s[i] == '#') skip++;
            else if (skip) skip--;
            else break;
            i--;
        }
    }

public:
    bool backspaceCompare(string s, string t) {
        int i = s.size() - 1, j = t.size() - 1;
        // backspace count
        int skips = 0, skipt = 0;
        while (i >= 0 || j >= 0){
            jump(s, i, skips);
            jump(t, j, skipt);
            if (i < 0 || j < 0) break;
            if (s[i--] != t[j--]) return false;
        }
        return i < 0 && j < 0;
    }
};

