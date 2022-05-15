/*
执行用时：7 ms, 在所有 Java 提交中击败了85.38% 的用户
内存消耗：41.8 MB, 在所有 Java 提交中击败了7.78% 的用户
通过测试用例：85 / 85
*/
class Solution {
    public int minDeletionSize(String[] strs) {
        int len = strs[0].length(), ans = 0;
        for (int i = 0; i < len; ++i) {
            char min = 'a';
            for (String s: strs) {
                if (s.charAt(i) >= min) {
                    min = s.charAt(i);
                } else {
                    ++ans;
                    break;
                }
            }
        }
        return ans;
    }
}
