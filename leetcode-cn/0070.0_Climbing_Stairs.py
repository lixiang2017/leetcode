'''
DP

执行用时：48 ms, 在所有 Python3 提交中击败了10.11% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了59.27% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


'''
DFS + memo

执行用时：40 ms, 在所有 Python3 提交中击败了10.11% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.85% 的用户
通过测试用例：45 / 45
'''
class Solution:

    @functools.lru_cache(50)
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n


'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了32.24% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了9.49% 的用户
通过测试用例：45 / 45
'''
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n in [1, 2]:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
