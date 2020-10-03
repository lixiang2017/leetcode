'''
You are here!
Your runtime beats 14.81 % of python submissions.
You are here!
Your memory usage beats 40.93 % of python submissions.
'''



class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        pairs_count = 0
        
        for i in xrange(size - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + k in nums[i + 1:]:
                pairs_count += 1
        return pairs_count