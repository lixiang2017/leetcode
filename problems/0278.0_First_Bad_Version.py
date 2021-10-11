'''
Binary Search
T: O(logN)
S: O(1)

Runtime: 36 ms, faster than 32.83% of Python3 online submissions for First Bad Version.
Memory Usage: 14.3 MB, less than 42.48% of Python3 online submissions for First Bad Version.
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
        
