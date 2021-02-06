'''
approach: Backtracking

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了57.46%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了77.84%的用户
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub = []
        size = len(nums)

        def backtracking(nums, begin, end, path):
            sub.append(path)

            for i in range(begin, end):
                backtracking(nums, i + 1, end, path + [nums[i]])

        backtracking(nums, 0, size, [])
        return sub
