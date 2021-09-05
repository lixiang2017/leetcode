/*
Brainteaser

执行用时：3 ms, 在所有 Java 提交中击败了41.67% 的用户
内存消耗：38.5 MB, 在所有 Java 提交中击败了54.17% 的用户
通过测试用例：106 / 106
*/
class Solution {
    public String orderlyQueue(String s, int k) {
        if (1 == k) {
            String ans = s;
            for (int i = 0; i < s.length(); ++i) {
                String ss = s.substring(i) + s.substring(0, i);
                if (ss.compareTo(ans) < 0) {
                    ans = ss;
                }
            }
            return ans;
        } else {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            return new String(chars);
        }
    }
}