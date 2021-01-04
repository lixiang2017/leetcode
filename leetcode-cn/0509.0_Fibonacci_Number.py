'''
执行结果：
通过
显示详情
执行用时：784 ms, 在所有 Python 提交中击败了17.07% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了11.42% 的用户
'''


class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in (0, 1): return n
        
        return self.fib(n - 1) + self.fib(n - 2)
    