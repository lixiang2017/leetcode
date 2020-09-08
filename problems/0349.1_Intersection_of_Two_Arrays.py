'''
Success
Details 
Runtime: 32 ms, faster than 75.79% of Python online submissions for Intersection of Two Arrays.
Memory Usage: 12 MB, less than 11.11% of Python online submissions for Intersection of Two Arrays.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        common = []
        #
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if (s1[i] < s2[j]):
                i += 1
                continue
            elif (s1[i] > s2[j]):
                j += 1
                continue
            else:
                common.append(s1[i])
                i += 1
                j += 1

        return list(set(common))

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print Solution().intersection(nums1, nums2)  # [2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print Solution().intersection(nums1, nums2)  # [9,4]
