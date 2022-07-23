'''
DP, T: O (N^2)=O(1000 * 1000), S:O(N*range)=O(1000 * 1000)
DP中记录最长序列长度

执行用时：4144 ms, 在所有 Python3 提交中击败了15.77% 的用户
内存消耗：22.8 MB, 在所有 Python3 提交中击败了89.93% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        # -500, 500
        # endswith nums[i], delta range from -500 to 500
        dp = [[1] * 1001 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                # nums[j] -> nums[i]
                d = nums[i] - nums[j]
                dp[i][d + 500] = max(dp[i][d + 500], dp[j][d + 500] + 1)
                ans = max(ans, dp[i][d + 500])
        return ans 


'''
return ans + 1
DP
DP中记录掐头（or 去尾）的长度

执行用时：4596 ms, 在所有 Python3 提交中击败了12.41% 的用户
内存消耗：22.7 MB, 在所有 Python3 提交中击败了96.64% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        # -500, 500
        # endswith nums[i], delta range from -500 to 500
        dp = [[0] * 1001 for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                # nums[j] -> nums[i]
                d = nums[i] - nums[j]
                dp[i][d + 500] = max(dp[i][d + 500], dp[j][d + 500] + 1)
                ans = max(ans, dp[i][d + 500])
        return ans + 1


'''
dp = [defaultdict(int) for _ in range(n)]

执行用时：5584 ms, 在所有 Python3 提交中击败了7.38% 的用户
内存消耗：46.3 MB, 在所有 Python3 提交中击败了45.30% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        # -500, 500
        # endswith nums[i], delta range from -500 to 500
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                # nums[j] -> nums[i]
                d = nums[i] - nums[j]
                dp[i][d + 500] = max(dp[i][d + 500], dp[j][d + 500] + 1)
                ans = max(ans, dp[i][d + 500])
        return ans + 1

