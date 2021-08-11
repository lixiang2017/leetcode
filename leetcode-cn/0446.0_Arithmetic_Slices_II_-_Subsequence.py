'''
Hash Table ＋ DP
Time: O(N^2)
Space: O(N^2)

执行用时：756 ms, 在所有 Python3 提交中击败了69.61% 的用户
内存消耗：68.5 MB, 在所有 Python3 提交中击败了35.29% 的用户
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        memo = [defaultdict(int) for _ in range(N)]
        total = 0
        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                total += memo[j][diff]
                memo[i][diff] += memo[j][diff] + 1

        return total
