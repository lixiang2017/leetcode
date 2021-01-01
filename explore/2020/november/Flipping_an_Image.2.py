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
            left, right = 0, len(row) - 1
            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left = left + 1
                right = right - 1
        return A
        