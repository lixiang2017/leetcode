'''
You are here!
Your runtime beats 63.82 % of python submissions.
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        cnt = 1
        for layer in range((n + 1) / 2):
            # direction 1 - traverse from left to right
            for ptr in range(layer, n - layer):
                matrix[layer][ptr] = cnt
                cnt += 1
            # direction 2 - traverse from top to bottom
            for ptr in range(layer + 1, n - layer):
                matrix[ptr][n - layer - 1] = cnt
                cnt += 1
            # direction 3 - traverse from right to left
            for ptr in range(layer + 1, n - layer):
                matrix[n - layer - 1][n - ptr - 1] = cnt
                cnt += 1
            # direction 4 - traverse from bottom to top
            for ptr in range(layer + 1, n - layer - 1):
                matrix[n - ptr - 1][layer] = cnt
                cnt += 1
        
        return matrix
