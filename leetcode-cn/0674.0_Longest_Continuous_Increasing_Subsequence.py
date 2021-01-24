'''
approach: Two Pointers
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了96.69%的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了37.60%的用户
'''

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        i = 0
        size = len(nums)

        while i < size:
            l = i
            while i + 1 < size and nums[i + 1] > nums[i]:
                i += 1
            longest = max(longest, i - l + 1)
            i += 1
            
        return longest
