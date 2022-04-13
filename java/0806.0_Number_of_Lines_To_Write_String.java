/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：39.5 MB, 在所有 Java 提交中击败了40.89% 的用户
通过测试用例：27 / 27
*/
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int[] ans = new int[2];
        ans[0] = 1;
        // int[] ans = {1, 0};
        for (char ch: s.toCharArray()) {
            ans[1] += widths[ch - 'a'];
            if (ans[1] > 100) {
                ans[1] = widths[ch - 'a'];
                ans[0]++;
            }
        }
        return ans;
    }
}



/*
执行用时：0 ms, 在所有 Java 提交中击败了100.00% 的用户
内存消耗：39.5 MB, 在所有 Java 提交中击败了39.88% 的用户
通过测试用例：27 / 27
*/
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        // int[] ans = new int[2];
        // ans[0] = 1;
        int[] ans = {1, 0};
        for (char ch: s.toCharArray()) {
            ans[1] += widths[ch - 'a'];
            if (ans[1] > 100) {
                ans[1] = widths[ch - 'a'];
                ans[0]++;
            }
        }
        return ans;
    }
}
