'''
approach: 2Dimension - DP
Time: O(MN)
Space: O(MN)

You are here!
Your runtime beats 65.79 % of python3 submissions.
You are here!
Your memory usage beats 82.06 % of python3 submissions.
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        common = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                common[i + 1][j + 1] = max(common[i][j + 1], common[i + 1][j])
                if word1[i] == word2[j]:
                    common[i + 1][j + 1] = max(common[i + 1][j + 1], common[i][j] + 1)
        
        return M + N - 2 * common[M][N]
