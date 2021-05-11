'''
approach 3: Sort Diagonals One by One Using Sort

Time: O((M + N) * (min(M, N) * 2 + min(M, N)log(min(M, N)) )) 
        =  O((M + N) * min(M, N) * log(min(M, N)))
Space: O(min(N, M))

You are here!
Your runtime beats 16.98 % of python submissions.
You are here!
Your memory usage beats 46.09 % of python submissions.

ref:
https://leetcode.com/problems/sort-the-matrix-diagonally/solution/
'''

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(mat), len(mat[0])
        
        def sort_diagonal(i, j):
            """
            Sort the current diagonal
            """
            diagonal = []
            # store the current diagonal in the list
            while i < n and j < m:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            
            # sort the diagonal values
            diagonal.sort()
            
            # push the sorted values back into the matrix
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = diagonal.pop()
        
        # sort all diagonals in the lower left corner
        for i in range(n):
            sort_diagonal(i, 0)
        # sort all diagonals in ther upper right corner
        for j in range(m):
            sort_diagonal(0, j)
        
        return mat
    