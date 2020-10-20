'''
Success
Details
Runtime: 20 ms, faster than 49.43% of Python online submissions for Rotate String.
Memory Usage: 13.5 MB, less than 19.01% of Python online submissions for Rotate String.
'''


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A * 2