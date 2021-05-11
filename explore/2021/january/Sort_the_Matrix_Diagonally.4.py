'''
approach 2: Sort Diagonals One by One Using Heap
Time: O(N * M * log(min(N, M)))
Space: O(min(N, M)), the longest diagonal contains not more than min(N, M) elements.

You are here!
Your runtime beats 13.75 % of python submissions.
You are here!
Your memory usage beats 92.18 % of python submissions.

ref:
https://leetcode.com/problems/sort-the-matrix-diagonally/solution/
'''


from heapq import heappush, heappop

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(mat), len(mat[0])
        
        def sort_diagonal(i, j):
            '''
            Sort the current diagonal
            '''
            diagonal = []
            # store the current diagonal
            # in the heap
            while i < n and j < m:
                # max heap -> to keep max element always on top
                heappush(diagonal, -mat[i][j])
                i += 1
                j += 1
            
            # push the sorted values
            # back to the matrix
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = -heappop(diagonal)
        
        # sort all diagonals
        # in the lower left cornet
        for i in range(n):
            sort_diagonal(i, 0)
        # sort all diagonals
        # in the upper right corner
        for j in range(m):
            sort_diagonal(0, j)
            
        return mat 
