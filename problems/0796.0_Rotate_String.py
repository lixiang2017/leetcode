'''
Success
Details
Runtime: 20 ms, faster than 49.43% of Python online submissions for Rotate String.
Memory Usage: 13.3 MB, less than 19.01% of Python online submissions for Rotate String.
'''

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        size_a, size_b = len(A), len(B)
        if size_a != size_b:
            return False
        if A == B: # ""  ""
            return True
        
        for i in xrange(1, size_a):
            if A[-i: ] + A[ : -i] == B:
                return True
        return False