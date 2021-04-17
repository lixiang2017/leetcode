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
