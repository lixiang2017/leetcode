'''
math + simulation

Runtime: 43 ms, faster than 80.67% of Python3 online submissions for Rotate Image.
Memory Usage: 14 MB, less than 29.99% of Python3 online submissions for Rotate Image.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # circle / round
        for cir in range(n // 2 + 1):
            # top-left, (cir, cir)
            # top-right, (cir, n - 1 - cir)
            # bottom-left, (n - 1 - cir, cir)
            # bottom-right, (n - 1 - cir, n - 1 - cir)
            for step in range(n - 1 - cir * 2):
                matrix[cir][cir + step],                        \
                matrix[cir + step][n - 1 - cir],                \
                matrix[n - 1 - cir][n - 1 - cir - step],        \
                matrix[n - 1 - cir - step][cir]                 \
                    =                                           \
                matrix[n - 1 - cir - step][cir],                \
                matrix[cir][cir + step],                        \
                matrix[cir + step][n - 1 - cir],                \
                matrix[n - 1 - cir][n - 1 - cir - step]

