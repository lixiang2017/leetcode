'''
Runtime: 188 ms, faster than 12.25% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 14.2 MB, less than 95.10% of Python3 online submissions for Sort the Matrix Diagonally.
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # diff = i - j 
        for diff in range(m - 1, -(n - 1) - 1, -1):
            diag = []
            for i in range(max(diff, 0), m):
                j = i - diff
                if j >= n:
                    break 
                diag.append(mat[i][j])
            diag.sort()
            # set 
            for i, x in zip(range(max(diff, 0), m), diag):
                j = i - diff
                if j >= n:
                    break 
                mat[i][j] = x 
        return mat 
