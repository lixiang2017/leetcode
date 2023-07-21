'''
DP
T: O(N^2)
S: O(N)

Runtime: 1122 ms, faster than 71.84% of Python3 online submissions for Number of Longest Increasing Subsequence.
Memory Usage: 16.6 MB, less than 52.88% of Python3 online submissions for Number of Longest Increasing Subsequence.
'''
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp
        longest_len = [1] * n
        longest_cnt = [1] * n
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    if longest_len[i] + 1 > longest_len[j]:
                        longest_len[j] = longest_len[i] + 1
                        longest_cnt[j] = longest_cnt[i]
                    elif longest_len[i] + 1 == longest_len[j]:
                        longest_cnt[j] += longest_cnt[i]
        m = max(longest_len)
        return sum(longest_cnt[i] for i in range(n) if longest_len[i] == m)
        
