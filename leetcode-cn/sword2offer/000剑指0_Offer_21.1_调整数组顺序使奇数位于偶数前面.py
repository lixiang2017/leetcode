'''
approach: Customize Sort

执行结果：通过
显示详情
执行用时：56 ms, 在所有 Python 提交中击败了11.45%的用户
内存消耗：18 MB, 在所有 Python 提交中击败了94.05%的用户
'''


class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(key=lambda num: num % 2, reverse=True)
        return nums
