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


'''
approach: Greedy
Time: O(N^2)
Space: O(1)

ref:
https://www.cnblogs.com/grandyang/p/6081984.html

执行用时：3032 ms, 在所有 Python 提交中击败了12.66%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了79.75%的用户
'''

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        i = j = k = 0
        while i < N:
            while i + 1 < N and nums[i] >= nums[i + 1]:
                i += 1
            j = i + 1
            while j + 1 < N and nums[j] <= nums[j + 1]:
                j += 1
            k = j + 1
            while k < N:
                if nums[i] < nums[k] and nums[k] < nums[j]:
                    return True
                k += 1

            i = j + 1

        return False
