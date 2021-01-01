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
        flip = []
        for row in A:
            reversed_row = row[::-1]
            inverted_row = [1 - item for item in reversed_row]
            flip.append(inverted_row)
        return flip
        