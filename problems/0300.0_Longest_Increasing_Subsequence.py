'''
Success
Details
Runtime: 996 ms, faster than 33.13% of Python online submissions for Longest Increasing Subsequence.
Memory Usage: 13.7 MB, less than 55.83% of Python online submissions for Longest Increasing Subsequence.
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print 'dp: ', dp
        # return dp[-1]  # Wrong Answer # [1,3,6,7,9,4,10,5,6]  # dp:  [1, 2, 3, 4, 5, 3, 6, 4, 5]
        return max(dp)
        