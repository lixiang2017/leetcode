'''
iteration

Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：12 ms, 在所有 Python 提交中击败了94.11% 的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了8.49% 的用户
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, second = 0, 1
        for i in range(n):
            first, second = second, first + second
        return first
        
    