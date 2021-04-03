'''
approach: Binary Search
Time: O(logN)
Space: O(1)

执行用时：16 ms, 在所有 Python 提交中击败了98.81%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了71.12%的用户
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = (right - left + 1) / 2 + left
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
        return left
        