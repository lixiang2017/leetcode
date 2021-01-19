'''
approach: Sort + Two Pointers
Time: O(NlogN + N) = O(NlogN)
Space: O(1)

You are here!
Your runtime beats 25.06 % of python submissions.
You are here!
Your memory usage beats 55.37 % of python submissions.
'''


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        operations = 0
        nums.sort()
        
        i, j = 0, size - 1
        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                operations += 1
                i += 1
                j -= 1
            elif total < k:
                i += 1
            else:
                j -= 1

        return operations
            