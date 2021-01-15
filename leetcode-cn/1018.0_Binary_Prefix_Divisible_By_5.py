'''
Bit Manipulation

Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：332 ms, 在所有 Python 提交中击败了74.65%的用户
内存消耗：
14 MB, 在所有 Python 提交中击败了73.24%的用户
'''

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        divisible = []
        num = 0
        for bit in A:
            num <<= 1
            num |= bit
            divisible.append(True if not (num % 5) else False)
        return divisible
            