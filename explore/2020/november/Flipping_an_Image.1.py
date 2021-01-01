'''
You are here!
Your runtime beats 70.47 % of python submissions.
'''


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for row in A:
            for i in xrange((len(row) + 1) / 2):
                '''
                In Python, the shortcur row[~i] = row[-i - 1] = row[len[row] - 1 - i]
                helps us find the i-th value of the row, counting from the right.
                '''
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A
        