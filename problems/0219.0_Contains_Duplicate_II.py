'''
approach: Hash Table + Two Pointers / Sliding Window
Time: O(N), one pass
Space: O(k), space for bucket

Runtime: 140 ms, faster than 5.26% of Python online submissions for Contains Duplicate II.
Memory Usage: 17.8 MB, less than 69.30% of Python online submissions for Contains Duplicate II.
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        bucket = {}
        for i, num in enumerate(nums):
            if num in bucket:
                return True
            bucket[num] = 1
            if i >= k:
                bucket.pop(nums[i - k])
                
        return False
                