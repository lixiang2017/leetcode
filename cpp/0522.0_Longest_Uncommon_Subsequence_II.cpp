/*
ref:
https://www.cnblogs.com/grandyang/p/6680548.html

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Longest Uncommon Subsequence II.
Memory Usage: 8.3 MB, less than 94.54% of C++ online submissions for Longest Uncommon Subsequence II.
*/

class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        int res = -1, j = 0, n = strs.size();
        for (int i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                if (i == j) continue;
                if (checkSubs(strs[i], strs[j])) break;
            }
            if (j == n)
                res = max(res, (int)strs[i].size());
        }
        return res;
    }
    int checkSubs(string subs, string str) {
        int i = 0;
        for (char c: str) {
            if (c == subs[i]) i ++;
            if (i == subs.size()) break;
        }
        return i == subs.size();
    }
};



/*
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Longest Uncommon Subsequence II.
Memory Usage: 8.5 MB, less than 33.45% of C++ online submissions for Longest Uncommon Subsequence II.
*/

class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        int n = strs.size();
        unordered_set<string> seen;
        sort(strs.begin(), strs.end(), [](string a, string b) {
            if (a.size() == b.size()) return a > b;
            return a.size() > b.size();
        }
        );
        
        for (int i = 0; i < n; i++) {
            if (i == n - 1 || strs[i] != strs[i + 1]) {
                bool found = true;
                
                for (auto a: seen) {
                    int j = 0;
                    for (char c: a) {
                        if (c == strs[i][j]) ++j;
                        if (j == strs[i].size()) break;
                    }
                    if (j == strs[i].size()) {
                        found = false;
                        break;
                    }
                }
                if (found)
                    return strs[i].size();
            }
            seen.insert(strs[i]);
        }
        return -1;
    }
};

