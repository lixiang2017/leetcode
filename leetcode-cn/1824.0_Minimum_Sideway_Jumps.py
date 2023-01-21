'''
DP
T: O(N)
S: O(N)

执行用时：4592 ms, 在所有 Python3 提交中击败了5.62% 的用户
内存消耗：85.1 MB, 在所有 Python3 提交中击败了39.33% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[inf] * 3 for _ in range(n + 1)]
        dp[0][0] = 1
        dp[0][1] = 0
        dp[0][2] = 1
        for i in range(1, n + 1):
            if obstacles[i - 1] == 0 and obstacles[i] == 0:
                for j in range(3):
                    dp[i][j] = dp[i - 1][j]
            else:
                for lane in range(1, 4):
                    if obstacles[i - 1] != lane and obstacles[i] != lane:
                        dp[i][lane - 1] = dp[i - 1][lane - 1]
            # from lane1 to lane2
            for l1 in range(3):
                for l2 in range(3):
                    if l1 != l2 and obstacles[i] != l1 + 1 and obstacles[i] != l2 + 1:
                        dp[i][l2] = min(dp[i][l2], dp[i][l1] + 1)

        return min(dp[-1])

