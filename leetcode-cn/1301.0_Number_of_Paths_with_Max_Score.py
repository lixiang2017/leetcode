class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 1_000_000_007
        m, n = len(board), len(board[0])
        max_sum = [[-inf] * (n + 1) for _ in range(m + 1)]
        ways = [[0] * (n + 1) for _ in range(m + 1)]
        max_sum[0][0] = 0
        ways[0][0] = 1

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == "X":
                    continue
                max_sum[i + 1][j + 1] = s = max(
                    max_sum[i][j], max_sum[i][j + 1], max_sum[i + 1][j]
                )
                if max_sum[i][j] == s:
                    ways[i + 1][j + 1] += ways[i][j]
                if max_sum[i][j + 1] == s:
                    ways[i + 1][j + 1] += ways[i][j + 1]
                if max_sum[i + 1][j] == s:
                    ways[i + 1][j + 1] += ways[i + 1][j]
                ways[i + 1][j + 1] %= MOD
                if ch.isdigit():
                    max_sum[i + 1][j + 1] += int(ch)

        return [max_sum[m][n], ways[m][n]] if max_sum[m][n] != -inf else [0, 0]
