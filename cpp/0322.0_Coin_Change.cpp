/*
DP

执行用时：88 ms, 在所有 C++ 提交中击败了38.72% 的用户
内存消耗：14.1 MB, 在所有 C++ 提交中击败了21.46% 的用户
通过测试用例：188 / 188
*/

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<unsigned int> dp(amount + 1, INT_MAX);
        dp[0] = 0;
        for (int j = 1; j <= amount; ++j) {
            for (int i = 0; i < coins.size(); ++i) {
                if (j >= coins[i])
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }
        if (INT_MAX == dp[amount]) {
            return -1;
        } else {
            return dp[amount];
        }
    }
};


/*
DP + memoization

执行用时：72 ms, 在所有 C++ 提交中击败了68.81% 的用户
内存消耗：15.5 MB, 在所有 C++ 提交中击败了15.77% 的用户
通过测试用例：188 / 188
*/
class Solution {
    vector<int> count;
    int dp(vector<int>& coins, int rem) {
        if (rem == 0) return 0;
        if (count[rem] != 0) return count[rem];
        int step = INT_MAX;
        for (int c: coins) {
            if (rem >= c) {
                int step1 = dp(coins, rem - c);
                if (step1 >= 0 && step1 + 1 < step)
                    step = step1 + 1;
            }
        }
        count[rem] = step == INT_MAX ? -1 : step;
        return count[rem];
    }
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount < 1) return 0;
        count.resize(amount + 1);
        return dp(coins, amount);
    }
};



