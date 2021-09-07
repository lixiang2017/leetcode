'''
柱状图，left二维数组预处理
Time: O(M^2 * N)
Space: O(MN)

执行用时：1728 ms, 在所有 Python3 提交中击败了5.83% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了27.03% 的用户
通过测试用例：71 / 71
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        # preprocess 2D-array left
        left = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '0':
                    continue
                if j == 0:
                    left[i][0] = 1
                else:
                    left[i][j] = left[i][j - 1] + 1
        
        ans = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == '0':
                    continue
                width = left[i][j]
                area = left[i][j]
                for k in range(i - 1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, (i - k + 1) * width)
                ans = max(ans, area)

        return ans
