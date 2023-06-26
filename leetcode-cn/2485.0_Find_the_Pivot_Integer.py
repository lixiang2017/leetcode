'''
执行用时：72 ms, 在所有 Python3 提交中击败了28.57% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了42.86% 的用户
通过测试用例：428 / 428
'''
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1 + n) * n // 2
        s = 0
        for i in range(1, n + 1):
            s += i 
            if s == total + i - s:
                return i 
            elif s > total + i - s:
                return -1
        return -1
        