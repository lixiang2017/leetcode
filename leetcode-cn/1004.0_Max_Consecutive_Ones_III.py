'''
approach: Sliding Window
滑动窗口 / 滑窗 / 虫取法
Time: O(N)
Space: O(1)

ref:
https://leetcode-cn.com/problems/max-consecutive-ones-iii/solution/fen-xiang-hua-dong-chuang-kou-mo-ban-mia-f76z/
'''

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        longest = 0
        left = right = 0
        zeros = 0
        N = len(A)
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1
        return longest
        