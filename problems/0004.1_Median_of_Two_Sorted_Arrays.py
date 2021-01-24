'''
ImportError: No module named statistics
    import statistics
Line 8 in findMedianSortedArrays (Solution.py)
    ret = Solution().findMedianSortedArrays(param_1, param_2)
Line 34 in _driver (Solution.py)
    _driver()
Line 44 in <module> (Solution.py)
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import statistics
        return statistics.median(nums1 + nums2)

    
if __name__ == '__main__':
    nums1 = [1, 3, 5 ,7, 9]
    nums2 = [2, 4 ,6 ,8 ,0]
    assert Solution().findMedianSortedArrays(nums1, nums2) == 4.5
