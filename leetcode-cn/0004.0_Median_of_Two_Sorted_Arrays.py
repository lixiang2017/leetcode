'''
执行用时：44 ms, 在所有 Python3 提交中击败了73.03% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了96.19% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        N = len(nums)
        if N % 2:
            return nums[N // 2]
        else:
            return (nums[N // 2] + nums[N//2 - 1]) / 2

'''
执行用时：40 ms, 在所有 Python3 提交中击败了85.87% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了14.72% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        M, N = len(nums1), len(nums2)
        i = j = 0
        nums = []
        while i < M and j < N:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < M:
            nums.extend(nums1[i:])
        if j < N:
            nums.extend(nums2[j:])
        L = M + N 
        if L % 2:
            return nums[L // 2]
        else:
            return (nums[L//2 - 1] + nums[L//2]) / 2


'''
binary search
二分range, 二分数组中的最大值最小值区间，其实就是二分答案
T: O(log(range) * (logM + logN)), range is 2 * 10^6
S: O(1)


执行用时：64 ms, 在所有 Python3 提交中击败了11.74% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了68.34% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        c = m + n 
        k = c // 2
        if c % 2:
            return self.findkth(nums1, nums2, k + 1)
        else:
            small = self.findkth(nums1, nums2, k)
            big = self.findkth(nums1, nums2, k + 1)
            return (small + big) / 2

    def findkth(self, nums1, nums2, k):
        if 0 == len(nums1):
            return nums2[k - 1]
        if 0 == len(nums2):
            return nums1[k - 1]
        start = min(nums1[0], nums2[0])
        end = max(nums1[-1], nums2[-1])
        while start <= end:
            mid = (start + end) // 2
            k1 = self.countSmallerEqual(nums1, mid)
            k2 = self.countSmallerEqual(nums2, mid)
            if k1 + k2 < k:
                start = mid + 1
            else:
                # so many same numbers in nums1 or nums2, so need to use >= k for answer
                # answer = mid, so return end + 1
                end = mid - 1             
        return end + 1

    def countSmallerEqual(self, nums, x):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        # index for [l-1], count l
        return l


'''
[1,3]
[2]
[1,2]
[3,4]
[0,0]
[0,0]

[0,0,0,0,0]
[-1,0,0,0,0,0,1]
'''


'''
T: O(log(min(M, N)))
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了98.03% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了80.44% 的用户
通过测试用例：2094 / 2094
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        infinity = 2 ** 40
        m, n = len(nums1), len(nums2)
        median1, median2 = 0, 0
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i 
            num_im1 = (-infinity if i == 0 else nums1[i - 1])
            num_i = (infinity if i == m else nums1[i])
            num_jm1 = (-infinity if j == 0 else nums2[j - 1])
            num_j = (infinity if j == n else nums2[j])
            if num_im1 <= num_j: # and num_jm1 <= num_i:
                median1, median2 = max(num_im1, num_jm1), min(num_i, num_j)
                left = i + 1
            else:
                right = i - 1
        
        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1



