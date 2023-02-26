/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：39.8 MB, 在所有 Java 提交中击败了17.42% 的用户
通过测试用例：70 / 70
*/
class Solution {
    public int minimumSwap(String s1, String s2) {
        int xy = 0, yx = 0;
        int n = s1.length();
        for (int i = 0; i < n; i++) {
            char a = s1.charAt(i), b = s2.charAt(i);
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
}
