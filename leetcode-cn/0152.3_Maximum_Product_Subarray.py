'''
It's actually a variant of Kadane's algorithm.

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了78.48% 的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了62.56% 的用户
'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix, suffix, max_so_far = 0, 0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            max_so_far = max(max_so_far, prefix, suffix)
        return max_so_far
        