'''
DP, T: O(N^2), S: O(N)

执行用时：160 ms, 在所有 Python3 提交中击败了7.01% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了60.43% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        # 以当前数为结尾的最长摆动长度
        pos_dp = [1] * n 
        neg_dp = [1] * n 
        # i ... j
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    pos_dp[j] = max(pos_dp[j], neg_dp[i] + 1)
                elif nums[i] > nums[j]:
                    neg_dp[j] = max(neg_dp[j], pos_dp[i] + 1)

        return max(pos_dp[-1], neg_dp[-1])

'''
DP, T: O(N), S: O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了84.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了28.17% 的用户
通过测试用例：26 / 26
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
