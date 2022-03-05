'''
T: O(N^2)
S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了76.88% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了98.27% 的用户
通过测试用例：21 / 21
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        n = len(m)
        # c: circle, every circle
        for c in range(n // 2):
            '''
            (c, c)   (c,   c+1) ....     (c, n - 1 - c)
            (c+1, c) (c+1, c+1) ....     (c+1, n - 1 - c)
            ... ...                              ...
            (n-1-c, c) (n-1-c, c+1) ...  (n-1-c, n -1 -c) 
            '''
            # every edge
            for step in range(n - 1 - c - c):
                m[c][c+step], m[c+step][n-1-c], m[n-1-c][n-1-c-step], m[n-1-c-step][c] = \
                    m[n-1-c-step][c], m[c][c+step], m[c+step][n-1-c], m[n-1-c][n-1-c-step]

'''
T: O(N^2)
S: O(1)
split every step/ variable

执行用时：36 ms, 在所有 Python3 提交中击败了50.75% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了47.29% 的用户
通过测试用例：21 / 21
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        n = len(m)
        # c: circle, every circle
        for c in range(n // 2):
            '''
            (c, c)   (c,   c+1) ....     (c, n - 1 - c)
            (c+1, c) (c+1, c+1) ....     (c+1, n - 1 - c)
            ... ...                              ...
            (n-1-c, c) (n-1-c, c+1) ...  (n-1-c, n -1 -c) 
            '''
            # every edge
            for step in range(n - 1 - c - c):
                up_left = m[c][c+step]                    # make room, backup
                m[c][c+step] = m[n-1-c-step][c]           # up_left = down_left
                m[n-1-c-step][c] = m[n-1-c][n-1-c-step]   # down_left = down_right
                m[n-1-c][n-1-c-step] = m[c+step][n-1-c]   # down_right = up_right
                m[c+step][n-1-c] = up_left                # up_right = up_left

