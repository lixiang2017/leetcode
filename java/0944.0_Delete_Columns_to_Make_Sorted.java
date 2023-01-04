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

/*
Runtime: 8 ms, faster than 93.03% of Java online submissions for Delete Columns to Make Sorted.
Memory Usage: 42.7 MB, less than 71.46% of Java online submissions for Delete Columns to Make Sorted.
*/
class Solution {
    public int minDeletionSize(String[] strs) {
        int K = strs[0].length();
        int answer = 0;
        // iterate over each index in the string
        for (int col = 0; col < K; col++) {
            for (int row = 1; row < strs.length; row++) {
                if (strs[row].charAt(col) < strs[row - 1].charAt(col)) {
                    answer++;
                    break;
                }
            }
        }
        return answer;        
    }
}
