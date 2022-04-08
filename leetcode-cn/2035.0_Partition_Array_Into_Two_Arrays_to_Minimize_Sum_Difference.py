'''
折半枚举 + two pointers + sort

执行用时：720 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了75.00% 的用户
通过测试用例：201 / 201
'''
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) >> 1
        ans = inf; total_sum = sum(nums)
        for l in range((n >> 1) + 1):
            left_comb = sorted(sum(left) for left in combinations(nums[: n], l))
            right_comb = sorted(sum(right) for right in combinations(nums[n: ], n - l))
            nn = len(left_comb)
            pl, pr = 0, nn - 1
            while pl < nn and pr >= 0:
                part_sum = left_comb[pl] + right_comb[pr]
                ans = min(ans, abs(total_sum - part_sum * 2))
                if ans in [0, 1]:
                    return ans 
                if part_sum < total_sum / 2:
                    pl += 1
                else:
                    pr -= 1

        return ans 
