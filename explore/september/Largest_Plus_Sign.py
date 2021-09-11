'''
Time: O(3 * N^2)
Space: O(4 * N^2)

You are here!
Your memory usage beats 49.83 % of python3 submissions.
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]
        mines_set = set(i * n + j for i, j in mines)
        
        # left and up
        for r in range(n):
            for c in range(n):
                if r * n + c not in mines_set:
                    if c > 0:
                        left[r][c] = left[r][c - 1] + 1
                    else:
                        left[r][c] = 1
                    if r > 0:
                        up[r][c] = up[r - 1][c] + 1
                    else:
                        up[r][c] = 1
        # right and down
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r * n + c not in mines_set:
                    if c < n - 1:
                        right[r][c] = right[r][c + 1] + 1
                    else:
                        right[r][c] = 1
                    if r < n - 1:
                        down[r][c] = down[r + 1][c] + 1
                    else:
                        down[r][c] = 1

        ans = 0
        for i in range(n):
            for j in range(n):
                arm = min(left[i][j], up[i][j], right[i][j], down[i][j])
                ans = max(ans, arm)
        return ans


'''
Brute Force
Time: O(N^3)

49 / 56 test cases passed.
    Status: Time Limit Exceeded
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in range(n):
            for c in range(n):
                k = 0
                while (k <= r < n - k and k <= c < n - k and
                    (r - k, c) not in banned and 
                    (r + k, c) not in banned and
                    (r, c + k) not in banned and
                    (r, c - k) not in banned):
                        k += 1
                ans = max(ans, k)
        return ans


'''

You are here!
Your memory usage beats 79.12 % of python3 submissions.
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * n for _ in range(n)]
        
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count
            count = 0
            for c in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if dp[r][c] > count: dp[r][c] = count
        
        ans = 0
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                if dp[r][c] > count: dp[r][c] = count
            count = 0
            for r in range(n - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if dp[r][c] > count: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
                
        return ans


