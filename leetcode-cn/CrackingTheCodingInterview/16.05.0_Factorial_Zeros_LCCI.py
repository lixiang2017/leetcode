'''
T:O(logN),S:O(1)
只需要计算有多少个5

执行用时：36 ms, 在所有 Python3 提交中击败了58.82% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了14.03% 的用户
通过测试用例：502 / 502
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        i = 5
        while i <= n:
            cnt += n // i
            i *= 5
        return cnt
