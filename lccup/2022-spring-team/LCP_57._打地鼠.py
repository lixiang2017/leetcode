'''
https://leetcode-cn.com/problems/ZbAuEH/
这个办法虽然过了，但是 O(81 * N) 的写法大概率过不了

执行用时：11988 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：39.6 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：63 / 63

自己比赛时超时的原因
1、不必要重新过滤出 time_set, 或使用 hash table记录 time -> positions
2、need 矩阵可以预计算出来，避免放在 for 的内层循环里每次都要计算
甚至可以把 need 提前计算出来，直接用
'''

class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        moles.sort(key = lambda m: m[0])
        n = len(moles)
        # every time, 9 states
        # dp = [[0] * 9 for _ in range(n + 1)]  # wrong
        dp = [[-float('inf')] * 9 for _ in range(n + 1)]
        dp[0][4] = 0
        # pre calculate
        need = [[0] * 9 for _ in range(9)]
        for prev in range(9):
            x, y = divmod(prev, 3)
            for cur in range(9):
                nx, ny = divmod(cur, 3)
                need[prev][cur] = abs(nx - x) + abs(ny - y)

        pre_t = 0
        for i in range(1, n + 1):
            t, x, y = moles[i - 1]
            diff = t - pre_t
            # prev state, cur state
            for prev in range(9):
                for cur in range(9):
                    if need[prev][cur] <= diff:
                        dp[i][cur] = max(dp[i][cur], dp[i - 1][prev])
            dp[i][3 * x + y] += 1
            pre_t = t 

        return max(dp[-1])

'''
[[1,1,0],[2,0,1],[4,2,2]]
[[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]
[[2,0,2],[6,2,0],[4,1,0],[2,2,2],[3,0,2]]
'''



'''
执行用时：11648 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：39.7 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：63 / 63
'''
class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        moles.sort(key = lambda m: m[0])
        # print(moles)
        n = len(moles)
        # every time, 9 states
        # dp = [[0] * 9 for _ in range(n + 1)]  # wrong
        dp = [[-float('inf')] * 9 for _ in range(n + 1)]
        dp[0][4] = 0
        # pre calculate
        need = [[0, 1, 2, 1, 2, 3, 2, 3, 4],
                [1, 0, 1, 2, 1, 2, 3, 2, 3],
                [2, 1, 0, 3, 2, 1, 4, 3, 2],
                [1, 2, 3, 0, 1, 2, 1, 2, 3],
                [2, 1, 2, 1, 0, 1, 2, 1, 2],
                [3, 2, 1, 2, 1, 0, 3, 2, 1],
                [2, 3, 4, 1, 2, 3, 0, 1, 2],
                [3, 2, 3, 2, 1, 2, 1, 0, 1],
                [4, 3, 2, 3, 2, 1, 2, 1, 0]]

        pre_t = 0
        for i in range(1, n + 1):
            t, x, y = moles[i - 1]
            diff = t - pre_t
            # prev state, cur state
            for prev in range(9):
                for cur in range(9):
                    if need[prev][cur] <= diff:
                        dp[i][cur] = max(dp[i][cur], dp[i - 1][prev])
            dp[i][3 * x + y] += 1
            pre_t = t 

        return max(dp[-1])


