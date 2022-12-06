/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：6.3 MB, 在所有 C++ 提交中击败了88.26% 的用户
通过测试用例：85 / 85
*/
class Solution {
public:
    int numDifferentIntegers(string word) {
        string s;
        unordered_set<string> st;
        for (char c : word) {
            if (isdigit(c)) {
                s += c;
            } else {
                if (s != "") st.insert(trim(s));
                s = "";
            }
        }
        if (s != "") st.insert(trim(s));
        return st.size();
    }

private:
    string trim(string &s) {
        int i = 0;
        while (i < s.size() - 1 && s[i] == '0') {
            i++;
        }
        return s.substr(i);
    }
};
