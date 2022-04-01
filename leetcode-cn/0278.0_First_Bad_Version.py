'''
binary search

执行用时：28 ms, 在所有 Python3 提交中击败了93.71% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了67.19% 的用户
通过测试用例：22 / 22
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



'''
执行用时：40 ms, 在所有 Python3 提交中击败了28.06% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.91% 的用户
通过测试用例：22 / 22
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
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return r 

