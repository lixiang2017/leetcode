/*
把乘法改成加法，每一次都计算贡献

执行用时：64 ms, 在所有 C++ 提交中击败了24.04% 的用户
内存消耗：11.1 MB, 在所有 C++ 提交中击败了70.19% 的用户
通过测试用例：76 / 76
*/
class Solution {
public:
    int uniqueLetterString(string s) {
        int n = s.length();
        long long ans = 0;
        for (char ch = 'A'; ch <= 'Z'; ch++) {
            for (int j = 0, l = -1, r = -1; j < n; ++j) {
                if (s[j] == ch) {
                    l = r, r = j;
                }
                ans += r - l;
            }
        }
        return ans;
    }
};



/*
执行用时：12 ms, 在所有 C++ 提交中击败了98.08% 的用户
内存消耗：11.1 MB, 在所有 C++ 提交中击败了75.96% 的用户
通过测试用例：76 / 76
*/
class Solution {
public:
    int uniqueLetterString(string s) {
        int n = s.length();
        uint64_t ans = 0;
        int pos[26][2];
        memset(pos, -1, sizeof(int) * 26 * 2);
        for (int i = 0; i < n; i++) {
            int now = s[i] - 'A';
            ans += (pos[now][1] - pos[now][0]) * (i- pos[now][1]);
            pos[now][0] = pos[now][1], pos[now][1] = i;
        }
        for (auto [l, r]: pos) ans += (n - r) * (r - l);
        return ans;
    }
};

