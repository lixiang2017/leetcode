'''
approach: Sort + Two Pointers
Time: O(NlogN + N)
Space: O(N), we are making copy of original array.

You are here!
Your runtime beats 69.67 % of python submissions.
You are here!
Your memory usage beats 96.31 % of python submissions.
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        N = len(nums)
        i, j = 0, N - 1
        while i < N and snums[i] == nums[i]:
            i += 1
        while j >= i and snums[j] == nums[j]:
            j -= 1
        
        return j - i + 1
