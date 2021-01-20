'''
approach: Sort
Time: O(NlogN)
Space: O(1)

执行结果：
通过
显示详情
执行用时：56 ms, 在所有 Python 提交中击败了76.51% 的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了11.11% 的用户
'''


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maximum = -sys.maxint
        mid1 = nums[0] * nums[1] * nums[-1]
        tail = nums[-3] * nums[-2] * nums[-1]
        maximum = max(maximum, mid1, tail)
        return maximum
