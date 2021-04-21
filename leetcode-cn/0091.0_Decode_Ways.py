'''
approach: DP / Iteration
Time: O(N)
Space: O(2N) = O(N)

dp[0][i] 表示以s[i]为结尾，并且仅仅以s[i]一个字母为有效解码分组的个数。s[0: i + 1]
dp[1][i] 表示以s[i]为结尾，并且以s[i - 1: i + 1]两个字母为有效解码分组的个数。s[0: i + 1]
所以最后为两种情况求和。

执行用时：52 ms, 在所有 Python3 提交中击败了10.90%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.56%的用户
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        N = len(s)
        dp = [[0] * N for _ in range(2)]
        dp[0][0] = 1
        dp[1][0] = 0

        for i in range(1, N):
            if 1 <= int(s[i]) <= 9:
                dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
            else:
                dp[0][i] = 0
            
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[1][i] = dp[0][i - 1]
            else:
                dp[1][i] = 0

        return dp[0][N - 1] + dp[1][N - 1]



'''
尝试了Recursion, 容易重复.
'''

'''
优化: 如果是0,不必再次赋值,因为初始化已经赋值过了. 去掉无用代码

执行用时：40 ms, 在所有 Python3 提交中击败了71.12%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.06%的用户
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        N = len(s)
        dp = [[0] * N for _ in range(2)]
        dp[0][0] = 1
        dp[1][0] = 0

        for i in range(1, N):
            if 1 <= int(s[i]) <= 9:
                dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
            
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[1][i] = dp[0][i - 1]

        return dp[0][N - 1] + dp[1][N - 1]



'''
approach: DP / Iteration
Time: O(N)
Space: O(1)

空间优化:状态压缩．经观察发现，每次迭代，只需要跟前一次状态进行比较．故使用四个变量即可．

执行用时：40 ms, 在所有 Python3 提交中击败了71.12%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了28.02%的用户
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        N = len(s)
        #dp = [[0] * N for _ in range(2)]
        #dp[0][0] = 1
        #dp[1][0] = 0
        presingle = 1
        predouble = 0
        single = double = 0

        for i in range(1, N):
            if 1 <= int(s[i]) <= 9:
                # dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
                single = presingle + predouble
            else:
                single = 0
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                # dp[1][i] = dp[0][i - 1]
                double = presingle
            else:
                double = 0
            presingle, predouble = single, double

        # return dp[0][N - 1] + dp[1][N - 1]
        return presingle + predouble

