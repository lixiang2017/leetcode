/*
执行用时：0 ms, 在所有 C 提交中击败了100.00% 的用户
内存消耗：5.5 MB, 在所有 C 提交中击败了40.74% 的用户
通过测试用例：70 / 70
*/
int minimumSwap(char * s1, char * s2){
    int xy = 0, yx = 0;
    int n = strlen(s1);
    for (int i = 0; i < n; i++) {
        char a = s1[i], b = s2[i];
        if (a == 'x' && b == 'y') {
            xy++;
        }
        else if (a == 'y' && b == 'x') {
            yx++;
        }
    }
    if (((xy + yx) & 1) == 1) {
        return -1;
    }
    return xy / 2 + yx / 2 + xy % 2 + yx % 2;
}
