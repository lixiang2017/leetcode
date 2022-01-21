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


'''
Time: O(1)
Space: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了76.68% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了63.68% 的用户
通过测试用例：106 / 106
'''
class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        # 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
        # 28， 28 + (q - 1) * 7
        m1 = (28 + 28 + (q - 1) * 7) * q // 2
        # 1 + q, 1 + q + r - 1
        m2 = (1 + q + q + r) * r // 2
        return m1 + m2
