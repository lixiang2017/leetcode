/*
执行用时：0 ms, 在所有 C++ 提交中击败了100.00% 的用户
内存消耗：9.9 MB, 在所有 C++ 提交中击败了75.66% 的用户
通过测试用例：63 / 63
*/
class Solution {
public:
    vector<string> letterCasePermutation(string s) {
        vector<string> ans;
        queue<string> q;
        q.emplace("");
        while (!q.empty()) {
            string &curr = q.front();
            if (curr.size() == s.size()) {
                ans.emplace_back(curr);
                q.pop();
            } else {
                int pos = curr.size();
                if (isalpha(s[pos])) {
                    string next = curr;
                    next.push_back(s[pos] ^ 32);
                    q.emplace(next);
                }
                curr.push_back(s[pos]);
            }
        }
        return ans;
    }
};
