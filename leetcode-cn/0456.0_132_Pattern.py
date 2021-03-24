'''
approach: Two Pointers, like 3 Sum
Time: O(N^2)
Space: O(1)

执行用时：2616 ms, 在所有 Python 提交中击败了12.66%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了22.79%的用户
'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        minimum = sys.maxint

        for j in range(N):
            minimum = min(minimum, nums[j])
            if minimum == nums[j]:
                continue

            for k in range(N - 1, j, -1):
                if minimum < nums[k] and nums[j] > nums[k]:
                    return True

        return False
