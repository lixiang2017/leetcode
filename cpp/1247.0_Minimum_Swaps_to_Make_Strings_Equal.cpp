/*
执行用时：4 ms, 在所有 C++ 提交中击败了36.71% 的用户
内存消耗：6.2 MB, 在所有 C++ 提交中击败了35.44% 的用户
通过测试用例：70 / 70
*/
class Solution {
public:
    int minimumSwap(string s1, string s2) {
        int xy = 0, yx = 0;
        int n = s1.length();
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
};
