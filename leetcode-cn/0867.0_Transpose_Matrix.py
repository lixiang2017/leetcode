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

'''
执行用时：
28 ms, 在所有 Python 提交中击败了94.41%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了90.37%的用户
'''

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*matrix)


'''
执行用时：
48 ms, 在所有 Python3 提交中击败了95.11%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了65.46%的用户
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))