'''
Success
Details
Runtime: 24 ms, faster than 35.09% of Python online submissions for Spiral Matrix II.
Memory Usage: 13.7 MB, less than 8.33% of Python online submissions for Spiral Matrix II.
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def floorMod(pos, size):
            return ((pos % size) + size) % size
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        cnt = 1
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direct = row = col = 0
        while cnt <= n * n:
            matrix[row][col] = cnt
            cnt += 1
            r = floorMod(row + direction[direct][0], n)
            c = floorMod(col + direction[direct][1], n)
            # change direction if next cell is non zero
            if matrix[r][c] != 0:
                direct = (direct + 1) % 4
            
            row += direction[direct][0]
            col += direction[direct][1]
            
        return matrix
    