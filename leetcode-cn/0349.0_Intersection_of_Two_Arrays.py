'''
approach: Hash Table
Time: O(N + M)

执行结果：
通过
显示详情
执行用时：32 ms, 在所有 Python 提交中击败了77.27%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了97.37%的用户
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash1 = {}
        for num in nums1:
            hash1[num] = True
        
        return list(set([num for num in nums2 if num in hash1]))
