'''
Bit Manipulation

Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：96 ms, 在所有 Python 提交中击败了85.92%的用户
内存消耗：
14 MB, 在所有 Python 提交中击败了59.15%的用户

ref:
https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/solution/ke-bei-5-zheng-chu-de-er-jin-zhi-qian-zh-asih/
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
            # num <<= 1
            # num |= bit
            # divisible.append(True if not (num % 5) else False)
            num = ((num << 1) | bit ) % 5
            divisible.append(num == 0)
        return divisible
            