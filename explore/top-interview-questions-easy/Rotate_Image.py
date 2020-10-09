'''
You are here!
Your runtime beats 96.65 % of python submissions.

1、此题需要一定的空间想象力
2、想不明白的话，可以剪一个方向的纸片，写上数字。折叠旋转几下就懂了
3、第一步选择正反对角线中的任意一条均可，第二步翻转每一行/或每一列即可
    ① 正对角线（左上 -- 右下），reverse each row
    ② 范对角线 (左下 -- 右上)，reverse each column
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose matrix
        for i in xrange(n):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse each row
        for i in xrange(n):
            matrix[i].reverse()