'''
DP
T: O(MN)
S: O(2 * N)

执行用时：44 ms, 在所有 Python3 提交中击败了6.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了82.35% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p1, p2 = [1] + [0] * (n - 1), [0] * n
        for _ in range(m):
            for i in range(n):
                if i > 0:
                    p2[i] = p2[i - 1] + p1[i]
                else:
                    p2[0] = p1[0]
            p1 = p2

        return p2[-1]
        
        
'''
执行用时：36 ms, 在所有 Python3 提交中击败了45.05% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.36% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
