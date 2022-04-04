/*
执行用时：1 ms, 在所有 Java 提交中击败了66.37% 的用户
内存消耗：39.3 MB, 在所有 Java 提交中击败了30.25% 的用户
通过测试用例：81 / 81
*/
class Solution {
    public int heightChecker(int[] heights) {
        int count = 0;
        int[] expected = heights.clone();
        Arrays.sort(expected);
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != expected[i])
                count++;
        }
        return count;
    }
}
