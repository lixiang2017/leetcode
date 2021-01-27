'''
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了63.86%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了61.45%的用户
'''

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = x_th = 0
        for i in range(n):
            if i % 7 == 0:
                x_th += 1
            current_base = x_th
            total += current_base + (i % 7)

        return total
