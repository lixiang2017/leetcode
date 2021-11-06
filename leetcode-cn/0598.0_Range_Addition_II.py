'''
执行用时：36 ms, 在所有 Python3 提交中击败了58.58% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了43.32% 的用户
通过测试用例：69 / 69
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n
        