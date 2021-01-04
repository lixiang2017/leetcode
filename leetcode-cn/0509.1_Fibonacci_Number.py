'''
DFS with memo  # recursion

Time: O(N)   # better than 0509.0
Space: O(N) + O(N)   # dict + stack

执行结果：
通过
显示详情
执行用时：1496 ms, 在所有 Python 提交中击败了5.14% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了11.42% 的用户
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0: 0, 1: 1}
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.fib(n - 1) + self.fib(n - 2)
            return memo[n]
        