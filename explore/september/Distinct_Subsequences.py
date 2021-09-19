'''
50 / 63 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
Last executed input: "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
"bddabdcae"

M: len(S)
Time: O(2^M)
这种暴力DFS，是暴力枚举了s的每一个子序列。顺便比较一下是否符合t。
中间有许多重复的计算，可以合并。
使用二维DP可以合并这些重复的计算，并计数。
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        L1, L2 = len(s), len(t)
        ans = 0
        
        def dfs(i, j):
            nonlocal ans
            if j == L2:
                ans += 1
                return
            if i >= L1:
                return
            
            if s[i] == t[j]:
                dfs(i + 1, j + 1)
                dfs(i + 1, j)
            else:
                dfs(i + 1, j)
        
        dfs(0, 0)
        return ans



'''
DP
Time: O(MN)
Space: O(MN)

You are here!
Your runtime beats 54.48 % of python3 submissions.
You are here!
Your memory usage beats 47.61 % of python3 submissions.
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        L1, L2 = len(s), len(t)
        dp = [[0] * L1 for _ in range(L2)]
        presum = [0] * L1
        for j in range(L1):
            if s[j] == t[0]:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
            if j == 0:
                presum[j] = dp[0][0]
            else:
                presum[j] = presum[j - 1] + dp[0][j]
        for i in range(1, L2):
            for j in range(L1):
                if j == 0:
                    presum[j] = dp[i - 1][j]
                else:
                    presum[j] = presum[j - 1] + dp[i - 1][j]
                    
                if s[j] == t[i]:
                    #if j == 0:  # wrong
                    #    dp[i][j] = 1
                    if j != 0:
                        dp[i][j] = presum[j - 1]
                else:
                    dp[i][j] = 0

        return sum(dp[-1])

