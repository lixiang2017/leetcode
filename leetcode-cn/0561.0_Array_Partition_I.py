'''
approach: Sort + Greedy
Time: O(NlogN)
Space: O(1)

执行结果：
通过
显示详情
执行用时：64 ms, 在所有 Python 提交中击败了82.14%的用户
内存消耗：14.7 MB, 在所有 Python 提交中击败了5.10%的用户
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(num for i, num in enumerate(nums) if not (i & 1))


'''
执行结果：
通过
显示详情
执行用时：60 ms, 在所有 Python 提交中击败了95.41%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了27.55%的用户
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
