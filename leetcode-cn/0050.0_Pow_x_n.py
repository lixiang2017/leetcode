'''
Brute Force

291 / 304 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
最后执行的输入：
0.00001
2147483647
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0 / x
            n = -n
        
        power = 1
        while n:
            power *= x
            n -= 1

        return power




'''
Divide and Conquer / Binary

approach: Recursion
Time: O(logN)
Space: O(1)

执行用时：24 ms, 在所有 Python 提交中击败了40.81%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了53.76%的用户
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0 / x
            n = -n
        
        if 0 == n:
            return 1
        
        if n & 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n >> 1)


'''
approach: Iteration
Time: O(logN)
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了67.08%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.18%的用户
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1.0 / x
            n = -n
        
        power = 1
        while n:
            if n & 1:
                n -= 1
                power *= x

            n >>= 1
            x *= x

        return power





'''
执行用时：24 ms, 在所有 Python 提交中击败了40.81%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了98.27%的用户
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


'''
执行用时：20 ms, 在所有 Python 提交中击败了67.08%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了44.76的用户
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x, n)

