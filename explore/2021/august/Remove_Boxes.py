'''
DP/DFS
l, r, k  # left, right, k mark the number of boxes which color equals right after right inddex

T: O(N^4)
S: O(N^3)

You are here!
Your runtime beats 24.11 % of python3 submissions.
You are here!
Your memory usage beats 66.52 % of python3 submissions.
'''

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            points = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    points = max(points, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            
            return points
        
        return dp(0, len(boxes) - 1, 0)


'''
DP/DFS
l, r, k  # left, right, k marks the number of boxes which color equals left before left index

T: O(N^4)
S: O(N^3)

'''

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            if l > r:
                return 0
            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1
            points = dp(l + 1, r, 0) + (k + 1) * (k + 1)
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    points = max(points, dp(i, r, k + 1) + dp(l + 1, i - 1, 0))
            
            return points
        
        return dp(0, len(boxes) - 1, 0)

'''
DP

ref:
https://leetcode-cn.com/problems/remove-boxes/solution/python3-ji-yi-hua-di-gui-he-dong-tai-gui-q1ak/

执行用时：4224 ms, 在所有 Python3 提交中击败了49.19% 的用户
内存消耗：27.7 MB, 在所有 Python3 提交中击败了54.84% 的用户
'''
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)
        dp = [[[0] * N for _ in range(N)] for _ in range(N)]

        for l in range(N - 1, -1, -1):
            for r in range(l, N):
                for k in range(N - r):
                    if r > l and boxes[r] == boxes[r - 1]:
                        dp[l][r][k] = dp[l][r - 1][k + 1]
                        continue
                    # 状态初始化：状态 dp[l][r][k] 不代表 boxes[r] 后面真的有 k 个颜色相
                    # 同的盒子，而是假设存在这么一种状态，并且把这种状态的最大值保留下来                   
                    dp[l][r][k] = dp[l][r - 1][0] + (k + 1) * (k + 1)
                    for i in range(l, r):
                        if boxes[i] == boxes[r]:
                            dp[l][r][k] = max(dp[l][r][k], \
                                    dp[l][i][k + 1] + dp[i + 1][r - 1][0])

        return dp[0][N - 1][0]


