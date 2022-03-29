'''
Runtime: 56 ms, faster than 88.54% of Python3 online submissions for Search in Rotated Sorted Array II.
Memory Usage: 14.4 MB, less than 63.51% of Python3 online submissions for Search in Rotated Sorted Array II.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
        