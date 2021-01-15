'''
Time: O(M + M + N)
Space: O(1)

You are here!
Your runtime beats 8.87 % of python submissions.
You are here!
Your memory usage beats 95.07 % of python submissions.
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # put nums in nums1 backwards
        # from m - 1 to 0, put to m+n-1 to n
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]
        
        # two pointers
        idx = 0
        j, k = n, 0
        while j < m + n and k < n:
            n1 = nums1[j]
            n2 = nums2[k]
            if n1 < n2:
                nums1[idx] = n1
                # nums1[j] = - sys.maxint # no need
                j += 1
            else:
                nums1[idx] = n2
                k += 1
            idx += 1
        
        # if k not reach n
        if k < n:
            nums1[idx: ] = nums2[k: ]
        
        