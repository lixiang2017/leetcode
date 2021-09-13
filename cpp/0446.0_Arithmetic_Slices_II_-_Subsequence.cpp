/*
DP
T: O(N^2)
S: O(N^2)

Runtime: 1153 ms, faster than 29.59% of C++ online submissions for Arithmetic Slices II - Subsequence.
Memory Usage: 135.4 MB, less than 69.15% of C++ online submissions for Arithmetic Slices II - Subsequence.
*/

#define LL long long
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size();
        LL ans = 0;
        vector<map<LL, int>> dp(n);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                LL delta = (LL)nums[i] - (LL)nums[j];
                int cnt = 0;
                if (dp[j].find(delta) != dp[j].end()) {
                    cnt = dp[j][delta];
                }
                dp[i][delta] += cnt + 1;
                ans += cnt;
            }
        }
        
        return (int)ans;
    }
};
