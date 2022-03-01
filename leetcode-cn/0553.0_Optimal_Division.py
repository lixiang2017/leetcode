'''
执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了64.29%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了50.00%的用户
'''

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if 1 == len(nums):
            return str(nums[0])
        elif 2 == len(nums):
            return  str(nums[0]) + '/' +  str(nums[1])
        else:
            return str(nums[0]) + '/(' + '/'.join([str(num) for num in nums[1:]]) + ')'


'''
执行用时：44 ms, 在所有 Python3 提交中击败了21.19% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.46% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        if len(nums) < 3:
            return '/'.join(nums)
        return nums[0] + '/(' + '/'.join(nums[1: ]) + ')'
        