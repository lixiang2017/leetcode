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
