'''
approach: DP
Time: O(2N) = O(N)
Space: O(2N) = O(N)

执行用时：36 ms, 在所有 Python3 提交中击败83.86%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.62%的用户
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return nums[0]

        max1 = max2 = 0
        dp1 = [[0] * N for _ in range(2)]
        # from 1 to n - 1, i.e. 0 to n - 2
        ## not rob
        dp1[0][0] = 0
        ## rob
        dp1[1][0] = nums[0]
        for i in range(1, N - 1):
            dp1[0][i] = max(dp1[0][i - 1], dp1[1][i - 1])
            dp1[1][i] = dp1[0][i - 1] + nums[i]
        max1 = max(dp1[0][N - 2], dp1[1][N - 2])

        # from 2 to n, i.e. 1 to n - 1
        dp1 = [[0] * N for _ in range(2)]
        ## not rob
        dp1[0][1] = 0
        ## rob
        dp1[1][1] = nums[1]
        for i in range(2, N):
            dp1[0][i] = max(dp1[0][i - 1], dp1[1][i - 1])
            dp1[1][i] = dp1[0][i - 1] + nums[i]
        max2 = max(dp1[0][N - 1], dp1[1][N - 1])
        return max(max1, max2)
        