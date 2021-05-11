'''
135 / 138 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
 [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
 [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
 [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
 [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
 [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
 [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
 [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
 [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
 [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        longest = [[1] * N for _ in range(M)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(i, j):
            if i < 0 or i > M or j < 0 or j > N:
                return 0
            for deltax, deltay in directions:
                nx = i + deltax
                ny = j + deltay
                if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] > matrix[i][j]:
                    longest[i][j] = max(longest[i][j], dfs(nx, ny) + 1)
            return longest[i][j]                    
        
        for i in range(M):
            for j in range(N):
                longest[i][j] = dfs(i, j)
        
        return max([max(row) for row in longest])


'''
approach: DFS + Memorization

You are here!
Your runtime beats 62.21 % of python submissions.
You are here!
Your memory usage beats 86.30 % of python submissions.
'''



class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        longest = [[1] * N for _ in range(M)]
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(i, j):
            if longest[i][j] != 1:    # memorization
                return longest[i][j]
            if i < 0 or i > M or j < 0 or j > N:
                return 0
            for deltax, deltay in directions:
                nx = i + deltax
                ny = j + deltay
                if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] > matrix[i][j]:
                    longest[i][j] = max(longest[i][j], dfs(nx, ny) + 1)
            return longest[i][j]                    
        
        for i in range(M):
            for j in range(N):
                longest[i][j] = dfs(i, j)
        
        return max([max(row) for row in longest])
    




    