'''
Time: O(NlogN)
Space: O(1)

You are here!
Your runtime beats 97.96 % of python submissions.
You are here!
Your memory usage beats 41.71 % of python submissions
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse = True)
        return nums[k - 1]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[-1 * k]
        