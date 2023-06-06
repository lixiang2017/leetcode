'''
执行用时：56 ms, 在所有 Python3 提交中击败了92.20% 的用户
内存消耗：20.4 MB, 在所有 Python3 提交中击败了56.34% 的用户
通过测试用例：72 / 72
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = Counter()
        for col in zip(*grid):
            c[tuple(col)] += 1
        ans = 0
        for row in grid:
            t = tuple(row)
            ans += c[t]
        return ans 
        