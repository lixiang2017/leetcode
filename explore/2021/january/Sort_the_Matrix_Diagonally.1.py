'''
Time: O((M + N) * (M+N)log(M+N) )
Space: O(M + N)


You are here!
Your runtime beats 81.94 % of python submissions
You are here!
Your memory usage beats 19.95 % of python submissions.
'''

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat: return []
        if not mat[0]: return [[]]
        
        m, n = len(mat), len(mat[0])
        # ascending = [[0 for _ in range(n)] for _ in range(m)]
        # row
        for i in range(m):
            current_i = i
            j = 0
            diagonal = []
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()
            # set value
            j = 0
            while current_i < m and j < n:
                mat[current_i][j] = diagonal.pop(0)
                current_i += 1
                j += 1
        
        # column
        for j in range(1, n):
            current_j = j
            i = 0
            diagonal = []
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()
            # set value
            i = 0
            while i < m and current_j < n:
                mat[i][current_j] = diagonal.pop(0)
                i += 1
                current_j += 1
        
        # return ascending
        return mat
