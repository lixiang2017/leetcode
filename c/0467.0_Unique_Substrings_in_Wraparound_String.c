/*
执行用时：4 ms, 在所有 C 提交中击败了72.41% 的用户
内存消耗：6 MB, 在所有 C 提交中击败了31.03% 的用户
通过测试用例：81 / 81
*/

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int findSubstringInWraproundString(char * p){
    int dp[26];
    int len = strlen(p);
    memset(dp, 0, sizeof(dp));
    int k = 0;
    for (int i = 0; i < len; ++i) {
        if (i && (p[i] - p[i - 1] + 26) % 26 == 1) {
            ++k;
        } else {
            k = 1;
        }
        dp[p[i] - 'a'] = MAX(dp[p[i] - 'a'], k);
    }
    int res = 0;
    for (int i = 0; i < 26; i++) {
        res += dp[i];
    }
    return res;
}
