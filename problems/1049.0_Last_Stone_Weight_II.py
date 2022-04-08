'''
positive_part a, negative_part b
a + b = total_sum
a - b = diff = ans
suppose a >= b
2 * a = total_sum + ans
a = (total_sum + ans) // 2


01背包 knapsack
dp[i][j] 表示 第i个石头选择与否，当前和(cur_sum) 等于j时，能否达到的状态。
若dp[i][j]为True表示这个状态可以达到; 如果为False,则无法达到。
初始状态，即和为0的状态都可以到达。即，第一列均为True。

每次计算dp[i][j]都尽可能让其为True。两种选择。
1、每次迭代更新时，都可以不选择这个数字进入加和，即 dp[i][j] = dp[i - 1][j]，状态与上一行一致。继承自上一行。
2、选择这个数字进入加和，则需要 j >= stones[i - 1] 才行。同时更新dp[i][j]。

更新这个二维表格从左至右，从上到下，一行行更新。
最后只需要根据最后一行结果，即处理了所有数字。从half_sum降序查找能否到达True。

T: O(N * sum(stones))
S: O(N * sum(stones) // 2)

Accepted    84 ms   14.3 MB python3
'''

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        half_sum = total_sum // 2
        n = len(stones)
        dp = [[False] * (half_sum + 2) for _ in range(n + 1)]
        # the first column
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n + 1):  # stones[i - 1]
            for j in range(half_sum + 2):
                dp[i][j] = dp[i - 1][j]
                if j >= stones[i - 1]:
                    dp[i][j] |= dp[i - 1][j - stones[i - 1]] 
        
        for x in range(half_sum, -1, -1):
            if dp[n][x]:
                return total_sum - x - x
        return -1


'''
空间可以压缩成一维，但是第二维度需要从后面处理。
for j in range(half_sum + 1, stones[i - 1] - 1, -1):
这样避免多次使用当前石头。
比如当前石头重量为3，dp[5]为True。如果正向处理，dp[8] dp[11] dp[14] dp[17]...都变成True了。这一直用了当前石头。但是当前石头只能用一次。

Runtime: 56 ms, faster than 86.73% of Python3 online submissions for Last Stone Weight II.
Memory Usage: 13.9 MB, less than 73.46% of Python3 online submissions for Last Stone Weight II.
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        half_sum = total_sum // 2
        n = len(stones)
        dp = [False] * (half_sum + 2) 
        # the first column
        dp[0] = True
        
        for i in range(1, n + 1):  # stones[i - 1]
            for j in range(half_sum + 1, stones[i - 1] - 1, -1):
                dp[j] |= dp[j - stones[i - 1]] 
        
        for x in range(half_sum, -1, -1):
            if dp[x]:
                return total_sum - x - x
        return -1


