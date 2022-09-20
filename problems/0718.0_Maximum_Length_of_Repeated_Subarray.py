'''
DP
T: O(MN)
S: O(MN)

Runtime: 6597 ms, faster than 40.41% of Python3 online submissions for Maximum Length of Repeated Subarray.
Memory Usage: 39.2 MB, less than 74.09% of Python3 online submissions for Maximum Length of Repeated Subarray.
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if nums2[i] == nums1[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1 
        return max(max(row) for row in dp)
