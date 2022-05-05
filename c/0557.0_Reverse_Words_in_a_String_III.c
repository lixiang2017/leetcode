/*
执行用时：8 ms, 在所有 C 提交中击败了53.99% 的用户
内存消耗：6.9 MB, 在所有 C 提交中击败了48.55% 的用户
通过测试用例：29 / 29
*/
char * reverseWords(char * s){
        int i = 0, n = strlen(s);
        while (i < n) {
            int start = i;
            while (i < n && s[i] != ' ') {
                i++;
            }
            int l = start, r = i - 1;
            while (l < r) {
                char tmp = s[l];
                s[l] = s[r];
                s[r] = tmp;
                l++, r--;
            }
            while (i < n && s[i] == ' ') {
                i++;
            }
        }
        return s;
}

