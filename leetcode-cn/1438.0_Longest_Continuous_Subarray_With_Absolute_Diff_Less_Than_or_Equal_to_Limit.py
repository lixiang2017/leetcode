'''
approach: SortedList + Sliding Window
Time: O(NlogN)
Space: O(N)

执行结果：通过
显示详情
执行用时：1240 ms, 在所有 Python 提交中击败了5.13%的用户
内存消耗：18.1 MB, 在所有 Python 提交中击败了66.67%的用户

ref:
https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/jue-dui-chai-bu-chao-guo-xian-zhi-de-zui-5bki/
https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/solution/he-gua-de-shu-ju-jie-gou-hua-dong-chuang-v46j/
'''

from sortedcontainers import SortedList

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        s = SortedList()
        N = len(nums)
        left = right = longest = 0
        while right < N:
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            longest = max(longest, right - left + 1)
            right += 1

        return longest
