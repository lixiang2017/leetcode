'''
Two Pointers

Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了67.14% 的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了88.04% 的用户
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        size = len(nums)
        i = 0
        while i < size:
            j = i
            while j + 1 < size and nums[j + 1] == nums[j] + 1:
                j += 1

            if i == j:
                ranges.append(str(nums[i]))
            else:
                ranges.append(str(nums[i]) + '->' + str(nums[j]))

            i = j + 1

        return ranges
        