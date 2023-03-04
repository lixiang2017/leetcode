/*
Runtime: 5 ms, faster than 6.17% of C online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 5.7 MB, less than 68.08% of C online submissions for Find the Index of the First Occurrence in a String.
*/
int strStr(char * haystack, char * needle){
    int m = strlen(needle);
    int n = strlen(haystack);
    for (int windowStart = 0; windowStart <= n - m; windowStart++) {
        for (int i = 0; i < m; i++) {
            if (needle[i] != haystack[windowStart + i]) {
                break;
            }
            if (i == m - 1) {
                return windowStart;
            }
        }
    }
    return -1;
}
