'''
approach: Bit Manipulation, XOR
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：28 ms, 在所有 Python 提交中击败了72.75%的用户
内存消耗：14.8 MB, 在所有 Python 提交中击败了27.11%的用户
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(lambda x, y: x ^ y, nums)
        