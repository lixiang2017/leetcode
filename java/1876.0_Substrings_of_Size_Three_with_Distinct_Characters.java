/*
执行用时：1 ms, 在所有 Java 提交中击败了74.68% 的用户
内存消耗：39.2 MB, 在所有 Java 提交中击败了60.16% 的用户
通过测试用例：160 / 160
*/

class Solution {
    public int countGoodSubstrings(String s) {
        int count = 0;
        for (int i = 1; i < s.length() - 1; i++) {
            if (isGood(s.charAt(i - 1), s.charAt(i), s.charAt(i + 1)))
                count++;
        }
        return count;
    }

    private boolean isGood(char c1, char c2, char c3) {
        return c1 != c2 && c1 != c3 && c2 != c3;
    }
}
