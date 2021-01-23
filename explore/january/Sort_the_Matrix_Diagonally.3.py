'''
approach 1: HashMap of Heaps

Time complexity: O(N * M * log(min(N, M))), where N is a number of rows and M is a number of columns. 
We perform N * M operations in two nested loops. At each iteration, we push an element into a heap that
contains not more than min(N, M) elements.

Space complexity: O(N * M) to keep the hashmap with all input elements, where N is a number of rows and 
M is a number of columns.

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
        # hashmap to keep the diagonals
        heap = defaultdict(list)
        
        # fill the hashmap
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                heappush(heap[i - j], val)
                # heap[i - j].append(val)
            
        # for key in heap:
        #     heap[key].sort(reverse=True)
        
        # build output
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                # mat[i][j] = heap[i - j].pop()
                mat[i][j] = heappop(heap[i - j])
        
        return mat
    