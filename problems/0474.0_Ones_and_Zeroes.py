'''
DP
背包问题

Runtime: 7744 ms, faster than 6.94% of Python3 online submissions for Ones and Zeroes.
Memory Usage: 14.3 MB, less than 55.99% of Python3 online submissions for Ones and Zeroes.
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        size = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # preprocess
        cnt = [[0, 0] for _ in range(size + 1)]
        # cnt = [Counter(one_str) for one_str in strs]
        for i, one_str in enumerate(strs):
            one = zero = 0
            for ch in one_str:
                if ch == '0':
                    zero += 1
                else:
                    one += 1
            cnt[i + 1] = [zero, one]
        
        for i in range(1, size + 1):
            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    # not choose i_th str
                    dp[j][k] = dp[j][k]
                    # if can choose i_th str
                    if j >= cnt[i][0] and k >= cnt[i][1]:
                        dp[j][k] = max(dp[j][k], dp[j - cnt[i][0]][k - cnt[i][1]] + 1)
        
        return dp[m][n]


