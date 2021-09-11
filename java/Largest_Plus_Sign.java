/*
53 / 56 test cases passed.
	Status: Time Limit Exceeded
*/

class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        Set banned = new HashSet<>();
        for (int[] mine: mines) {
            banned.add(mine[0] * n + mine[1]);
        }
        int ans = 0;
        for (int r = 0; r < n; ++r) for (int c = 0; c < n; ++c) {
            int k = 0;
            while (k <= r && r < n - k && k <= c && c < n - k &&
                  !banned.contains((r - k) * n + c) &&
                  !banned.contains((r + k) * n + c) &&
                  !banned.contains(r * n + c - k) &&
                  !banned.contains(r * n + c + k))
                k += 1;
            ans = Math.max(ans, k);
        }
        
        return ans;
    }
}


/*
You are here!
Your runtime beats 12.11 % of java submissions.
*/

class Solution {
    public int orderOfLargestPlusSign(int n, int[][] mines) {
        Set<Integer> banned = new HashSet<>();
        for (int[] mine: mines) {
            banned.add(mine[0] * n + mine[1]);
        }
        int ans = 0, count = 0;
        int[][] dp = new int[n][n];
        for (int r = 0; r < n; ++r) {
            count = 0;
            for (int c = 0; c < n; ++c) {
                count = banned.contains(r*n + c) ? 0: count + 1;
                dp[r][c] = count;
            }
            count = 0;
            for (int c = n - 1; c >= 0; --c) {
                count = banned.contains(r*n + c) ? 0: count + 1;
                dp[r][c] = Math.min(dp[r][c], count);
            }
        }
        
        for (int c = 0; c < n; ++c) {
            count = 0;
            for (int r = 0; r < n; ++r) {
                count = banned.contains(r*n + c) ? 0: count + 1;
                dp[r][c] = Math.min(dp[r][c], count);
            }
            count = 0;
            for (int r = n - 1; r >= 0; --r) {
                count = banned.contains(r*n + c) ? 0: count + 1;
                dp[r][c] = Math.min(dp[r][c], count);
                ans = Math.max(dp[r][c], ans);
            }
        }
        return ans;
    }
}

