'''

You are here!
Your runtime beats 99.19 % of python submissions.
You are here!
Your memory usage beats 9.43 % of python submissions.
'''


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = defaultdict(list)
        
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                heap[i - j].append(val)
            
        for key in heap:
            heap[key].sort(reverse=True)
        
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                mat[i][j] = heap[i - j].pop()
        
        return mat
    