'''
Time: O(M * N)
Space: O(M * N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了97.50%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了29.48%的用户
'''


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N = len(matrix), len(matrix[0])
        trans = [[0] * M for _ in range(N)]
        for i in range(M):
            for j in range(N):
                trans[j][i] = matrix[i][j]
        return trans
