'''
T:O(logN),S:O(1)
只需要计算有多少个5

执行用时：40 ms, 在所有 Python3 提交中击败了57.59% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.48% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        i = 5
        while i <= n:
            cnt += n // i
            i *= 5
        return cnt
