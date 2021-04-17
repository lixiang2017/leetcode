'''
Brute Force
Time: O(N^2)
Space: O(1)

51 / 54 个通过测试用例
状态：超出时间限制
提交时间：1 分钟前
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, i + k + 1):
                if j < N:
                    if abs(nums[i] - nums[j]) <= t:
                        return True
        return False


'''
approach: Bucket + Hash Table + Two Pointers
Time: O(N)
Space: O(k)

执行用时：76 ms, 在所有 Python3 提交中击败了25.12%的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了24.14%的用户
'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def getIdx(num):
            return (num + 1) / size - 1 if num < 0 else num / size

        bucket = {}
        size = t + 1
        for i, num in enumerate(nums):
            idx = getIdx(num)
            if idx in bucket:
                return True
            left, right = idx - 1, idx + 1
            if left in bucket and abs(num - bucket[left]) <= t:
                return True
            if right in bucket and abs(num - bucket[right]) <= t:
                return True
            bucket[idx] = num
            if i >= k:
                bucket.pop(getIdx(nums[i - k]))

        return False
