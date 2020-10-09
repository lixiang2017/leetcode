'''
You are here!
Your runtime beats 82.29 % of python submissions.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = {}
        size = len(nums)
        for i in xrange(size):
            if nums[i] in ans:
                return [ans[nums[i]], i]
            ans[target - nums[i]] = i