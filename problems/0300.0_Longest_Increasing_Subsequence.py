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


'''
DP
T: O(N^2)
S: O(N)

Runtime: 5604 ms, faster than 20.91% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14 MB, less than 99.41% of Python3 online submissions for Longest Increasing Subsequence.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


'''
binary search
T: O(NlogN)
S: O(N)

Runtime: 89 ms, faster than 90.31% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.3 MB, less than 48.57% of Python3 online submissions for Longest Increasing Subsequence.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 == n:
            return 0
        f = [nums[0]]
        for i in range(1, n):
            if nums[i] > f[-1]:
                f.append(nums[i])
            else:
                idx = bisect_left(f, nums[i])
                f[idx] = nums[i]
        return len(f)


'''
binary search
T: O(NlogN)
S: O(N)

Runtime: 96 ms, faster than 87.65% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.3 MB, less than 48.57% of Python3 online submissions for Longest Increasing Subsequence.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = []
        for i in range(n):
            if not f or nums[i] > f[-1]:
                f.append(nums[i])
            else:
                idx = bisect_left(f, nums[i])
                f[idx] = nums[i]
        return len(f)




