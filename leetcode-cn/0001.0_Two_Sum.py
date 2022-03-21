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

'''
hash table
T: O(N)
S: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了59.06% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了27.18% 的用户
通过测试用例：57 / 57
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2idx = dict()
        for i, x in enumerate(nums):
            if target - x in num2idx:
                return [i, num2idx[target - x]]
            num2idx[x] = i 
        return []

