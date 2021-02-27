'''
approach: Bit Manipulation
Time: O(N * 2 ^ N), where N is the number of nums.
Space: O(N * 2 ^ N)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了81.31%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了45.73%的用户
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub = []
        size = len(nums)
        for i in range(2 ** size):
            possible = []
            for j in range(size):
                if (i >> j) & 1: 
                    possible.append(nums[j])
            sub.append(possible)

        return sub


'''
执行用时：16 ms, 在所有 Python 提交中击败了82.35%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了32.72%的用户
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sub = [[]]
        for num in nums:
            sub += [item + [num] for item in sub]
        return sub
