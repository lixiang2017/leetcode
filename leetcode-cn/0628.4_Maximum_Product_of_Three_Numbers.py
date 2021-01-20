'''
执行结果：
通过
显示详情
执行用时：44 ms, 在所有 Python 提交中击败了96.83% 的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了50.48% 的用户
'''

import heapq
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlargest = heapq.nlargest(3, nums)
        nsmallest = heapq.nsmallest(2, nums)
        maximum = max(nsmallest[0] * nsmallest[1] * nlargest[0], \
            nlargest[0] * nlargest[1] * nlargest[2])
        return maximum
