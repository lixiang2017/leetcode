'''
比赛的时候，我是这样想的。
看起来有点像多维的背包问题。但是又无从下手。
每次如果尝试划分某一小块出去，还要记录每行都剩下几个。
这样剩下的不是一个标准的图形了，如何继续分类讨论 算下去，很麻烦。
遂放弃了。

啊啊啊啊啊，原来是我弄错题意了！！！
每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
    沿垂直方向按高度 完全 切割木块，或
    沿水平方向按宽度 完全 切割木块


To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces. 

中文题目的【完全】、英文题目的【entire】题目还给加粗了，是我理解错了。
题目的分割每次都是一分为二，而非每次抠一块地卖掉。
所以，是我自己想复杂了。完全可以枚举每一行，枚举每一列。


比赛后，题目提示。
Notice that cutting a piece breaks the problem down into smaller subproblems => DP 
可以把大问题分解为小问题，把大规模分解成小规模。
每次先算出小规模的最优解，慢慢推倒出大规模的最优解。
这个过程，抛弃了中间各种【非最优解】的大量讨论，而大大降低时间复杂度。
同时，避免了非矩形的讨论。同时保证了结果的正确性。
'''


'''
memo + DFS

执行用时：7924 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：32.2 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        d = {(h, w): p for h, w, p in prices}
        
        @cache
        def dfs(h, w):
            total = d.get((h, w), 0)
            for i in range(1, h):
                total = max(total, dfs(i, w) + dfs(h - i, w))
            for j in range(1, w):
                total = max(total, dfs(h, j) + dfs(h, w - j))
            return total
        
        return dfs(m, n)

'''
DP 
T: O(M * N * (M + N))
S: O(MN)

执行用时：6040 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # cut row
                for x in range(1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j] + dp[i - x][j])
                # cut column
                for y in range(1, j):
                    dp[i][j] = max(dp[i][j], dp[i][y] + dp[i][j - y])
        return dp[m][n]


