'''
Success
Details 
Runtime: 36 ms, faster than 99.71% of Python online submissions for Kth Largest Element in an Array.
Memory Usage: 14.2 MB, less than 84.21% of Python online submissions for Kth Largest Element in an Array.


'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]


'''
Runtime: 129 ms, faster than 28.76% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 71.94% of Python3 online submissions for Kth Largest Element in an Array.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]

'''
Runtime: 116 ms, faster than 38.34% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 40.94% of Python3 online submissions for Kth Largest Element in an Array.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heappush(h, x)
            if len(h) > k:
                heappop(h)
        return heappop(h)
        
'''
Runtime: 120 ms, faster than 35.24% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.9 MB, less than 21.53% of Python3 online submissions for Kth Largest Element in an Array.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heappush(h, x)
            if len(h) > k:
                heappop(h)
        return h[0]

