'''
Time Limit Exceeded

Submission Detail
11 / 22 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
Last executed input: 2126753390
1702766719

'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in xrange(1, n + 1):
            if isBadVersion(i):
                return i
            
