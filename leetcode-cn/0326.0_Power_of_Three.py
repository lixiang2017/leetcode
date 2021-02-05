'''
Time: O(logN)
Space: O(1)


执行结果：
通过
显示详情
执行用时：168 ms, 在所有 Python 提交中击败了88.33%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.00%的用户
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        while n:
            if n == 1: return True
            if n % 3: return False
            n /= 3

        return True
