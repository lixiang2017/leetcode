'''
presum + binary search

执行用时：60 ms, 在所有 Python3 提交中击败了95.14% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了5.98% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        presum = list(accumulate(chalk))
        k %= presum[-1]
        return bisect_right(presum, k)

