'''
approach: Backtracking
Time: O()

执行结果：通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了50.04%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了32.64%的用户
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        size = len(nums)
        def backtracking(nums, path, size):
            if len(path) == size:
                permutations.append(path)
                return
            for num in nums:
                if num not in path:
                    backtracking(nums, path + [num], size)

        backtracking(nums, [], size)
        return permutations
