'''
approach: Brute Force + Two Pointers
Time ;O(N ^ 2)
Space ;O(N)

执行用时：4920 ms, 在所有 Python 提交中击败了5.50%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了100.00%的用户
'''


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        greater = []

        i = 0
        while i < N:
            j = (i + 1) % N
            visitedCount = 0
            while nums[j] <= nums[i] and visitedCount < N:
                j = (j + 1) % N
                visitedCount += 1

            if visitedCount == N:
                greater.append(-1)
            else:
                greater.append(nums[j])

            i += 1

        return greater
