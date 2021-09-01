/*
执行用时：10 ms, 在所有 Java 提交中击败了7.44% 的用户
内存消耗：41.3 MB, 在所有 Java 提交中击败了5.21% 的用户
通过测试用例：168 / 168
*/

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> ans = new ArrayList<>();
        for(int[] interval: intervals) {
            int left = interval[0], right = interval[1];
            if (ans.size() == 0 || ans.get(ans.size() - 1)[1] < left)
                ans.add(new int[]{left, right});
            else
                ans.get(ans.size() - 1)[1] = Math.max(ans.get(ans.size() - 1)[1], right);
        }

        return ans.toArray(new int[ans.size()][]);
    }
}
