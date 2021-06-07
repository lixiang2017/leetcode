/*
DFS

执行用时：658 ms, 在所有 Java 提交中击败了17.82% 的用户
内存消耗：35.8 MB, 在所有 Java 提交中击败了88.07% 的用户
*/

class Solution {
    int ans = 0;
    public int findTargetSumWays(int[] nums, int target) {
        dfs(nums, target, 0, 0);
        return ans;
    }
    void dfs(int[] nums, int t, int u, int cur) {
        if (u == nums.length) {
            ans += cur == t ? 1 : 0;
            return;
        }
        dfs(nums, t, u + 1, cur + nums[u]);
        dfs(nums, t, u + 1, cur - nums[u]);
    }
}



/*
DFS

执行用时：696 ms, 在所有 Java 提交中击败了12.28% 的用户
内存消耗：35.6 MB, 在所有 Java 提交中击败了98.55% 的用户
*/

class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return dfs(nums, target, 0, 0);
    }
    int dfs(int[] nums, int t, int u, int cur) {
        if (u == nums.length) {
            return cur == t ? 1 : 0;
        }
        int add = dfs(nums, t, u + 1, cur + nums[u]);
        int minus = dfs(nums, t, u + 1, cur - nums[u]);
        return add + minus;
    }
}
