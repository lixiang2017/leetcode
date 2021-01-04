'''
iteration, use list

Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：8 ms, 在所有 Python 提交中击败了99.55% 的用户
内存消耗：13 MB, 在所有 Python 提交中击败了32.10% 的用户
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0, 1]
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]
    