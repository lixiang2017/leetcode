'''
approach: Two Monotonic Deques + Sliding Window
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：280 ms, 在所有 Python 提交中击败了97.44%的用户
内存消耗：17.8 MB, 在所有 Python 提交中击败了79.49%的用户

ref:
https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/jue-dui-chai-bu-chao-guo-xian-zhi-de-zui-5bki/
'''

from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        N = len(nums)
        left = right = longest = 0
        queMax = deque()  # decreasing
        queMin = deque()  # increasing
        while right < N:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            queMax.append(nums[right])
            queMin.append(nums[right])
            while queMin and queMax and queMax[0] - queMin[0] > limit:
                if nums[left] == queMax[0]:
                    queMax.popleft()
                if nums[left] == queMin[0]:
                    queMin.popleft()
                left += 1

            longest = max(longest, right - left + 1)
            right += 1
        return longest
