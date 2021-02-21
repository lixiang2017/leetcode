'''
approach: Iteration
Time: O(M * N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了76.29%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了56.70%的用户
'''

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                pos = i - j
                # pos > 0: bottom-left
                # pos = 0: diagonal
                # pos < 0: top-right
                if pos >= 0:
                    if matrix[i][j] != matrix[pos][0]:
                        return False
                else:
                    if matrix[i][j] != matrix[0][-pos]:
                        return False
        return True
