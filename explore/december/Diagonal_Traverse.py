'''
You are here!
Your runtime beats 62.99 % of python submissions.
'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        diagonal_order = []
        M, N = len(matrix), len(matrix[0])
        for i_plus_j in range(M + N - 1):
            if i_plus_j % 2 == 0:
                #
                if i_plus_j <= M - 1:
                    i, j = i_plus_j, 0
                else:
                    i, j = M - 1, i_plus_j - (M - 1) 
                    
                while 0 <= i <= M - 1 and 0 <= j <= N - 1:
                    diagonal_order.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                #
                if i_plus_j <= N - 1:
                    i, j = 0, i_plus_j
                else:
                    i, j = i_plus_j - (N - 1), N - 1
                    
                while 0 <= i <= M - 1 and 0 <= j <= N - 1:
                    diagonal_order.append(matrix[i][j])
                    i += 1
                    j -= 1
                    
        return diagonal_order
