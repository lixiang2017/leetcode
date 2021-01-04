'''
iteration, use dict

Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了44.26% 的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了60.65% 的用户
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0: 0, 1: 1}
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]
    