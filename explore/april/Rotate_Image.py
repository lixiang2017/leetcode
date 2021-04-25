'''

You are here!
Your runtime beats 94.83 % of python3 submissions.
You are here!
Your memory usage beats 84.23 % of python3 submissions.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*matrix[:: -1]))
        