'''
approach: Brute Force + Two Pointers
Time: O(M * N)
Space: O(M)

执行用时：176 ms, 在所有 Python 提交中击败了11.08%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了86.96%的用户
'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        greater = []
        M, N = len(nums1), len(nums2)
        i = 0
        while i < M:
            #
            j = 0
            pos = False
            gre = -1
            while j < N:
                if nums2[j] == nums1[i]:
                    pos = True
                if pos and nums2[j] > nums1[i]:
                    gre = nums2[j]
                    break
                j += 1 
            # append
            greater.append(gre)

            i += 1
        return greater



'''
approach: Mono Stack
Time: O(N + M + N) = O(M + N)
Space: O(M)

执行用时：20 ms, 在所有 Python 提交中击败了92.70%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了84.78%的用户
'''
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        greater = []
        hashMap = {num: -1 for num in nums2}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                hashMap[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            greater.append(hashMap[num]) 

        return greater
