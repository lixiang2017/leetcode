'''
two pointers, from larger numbers to smaller ones
T: O(M + N)
S: O(1)

Runtime: 59 ms, faster than 33.94% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 6.04% of Python3 online submissions for Merge Sorted Array.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        # left in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            
        
'''
T: O(N + (M+N)log(M+N) )
S: O(log(M+N)), recursion stack for sort

Runtime: 76 ms, faster than 9.50% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 14 MB, less than 37.34% of Python3 online submissions for Merge Sorted Array.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            nums1[-n: ] = nums2[:]
        nums1.sort()
            
        
