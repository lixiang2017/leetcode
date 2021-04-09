'''
approach: Math
Time: O(logN)
Space: (1)

执行用时：28 ms, 在所有 Python 提交中击败了54.39%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了24.56%的用户
'''

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if 0 == n:
            return False
            
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n /= factor
        return 1 == n

'''
Time: O(logN)
Space: (1)

执行用时：28 ms, 在所有 Python 提交中击败了54.39%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了89.12%的用户
'''

class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if 0 == n:  # not good
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n /= factor
        return 1 == n

