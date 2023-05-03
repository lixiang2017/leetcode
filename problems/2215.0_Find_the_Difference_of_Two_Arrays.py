'''
Runtime: 182 ms, faster than 61.53% of Python3 online submissions for Find the Difference of Two Arrays.
Memory Usage: 16.6 MB, less than 10.89% of Python3 online submissions for Find the Difference of Two Arrays.
'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
        
        