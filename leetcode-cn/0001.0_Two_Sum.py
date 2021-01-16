'''
apporach: hashmap
Time: O(N)
Space: O(N)

执行结果：通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了76.20%的用户
内存消耗：
12.9 MB, 在所有 Python 提交中击败了90.98%的用户
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        need = {}
        size = len(nums)
        for i in range(size):
            if nums[i] in need:
                return [i, need[nums[i]]]
            need[target - nums[i]] = i
