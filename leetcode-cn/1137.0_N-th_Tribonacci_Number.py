'''
DP

执行用时：28 ms, 在所有 Python3 提交中击败了89.02%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了75.36%的用户
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        for _ in range(n - 2):
            tri.append(sum(tri[-3:]))
        return tri[-1] if n > 2 else tri[n]
