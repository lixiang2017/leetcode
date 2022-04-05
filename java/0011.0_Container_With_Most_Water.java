/*
Runtime: 322 ms, faster than 5.29% of Java online submissions for Container With Most Water.
Memory Usage: 81.4 MB, less than 30.57% of Java online submissions for Container With Most Water.
*/

class Solution {
    public int maxArea(int[] height) {
        int n = height.length, ans = 0;
        for (int i = 1; i < n; i++) {
            if (height[i] > ans / i)
            for (int j = 0; j < i; j++) {
                ans = Math.max(ans, Math.min(height[i], height[j]) * (i - j));
            }
        }
        return ans;
    }
}


/*
执行用时：4 ms, 在所有 Java 提交中击败了67.11% 的用户
内存消耗：50.9 MB, 在所有 Java 提交中击败了94.11% 的用户
通过测试用例：60 / 60
*/
class Solution {
    public int maxArea(int[] height) {
        int ans = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            ans = Math.max(ans, Math.min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }
        }
        return ans;
    }
}
