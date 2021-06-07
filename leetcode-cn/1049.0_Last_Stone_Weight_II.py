'''
DFS

78 / 86 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
最后执行的输入：
[89,23,100,93,82,98,91,85,33,95,72,98,63,46,17,91,92,72,77,79,99,96,55,72,24,98,79,93,88,92]
'''

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.last = 0x3f3f3f3f
        N = len(stones)
        def dfs(i, cur, N):
            if i == N:
                self.last = min(self.last, abs(cur))
                return
            # add
            dfs(i + 1, cur + stones[i], N)
            # minus
            dfs(i + 1, cur - stones[i], N)

        dfs(0, 0, N)
        return self.last


'''

执行用时：100 ms, 在所有 Python3 提交中击败了7.60% 的用户
内存消耗：23.7 MB, 在所有 Python3 提交中击败了5.12% 的用户
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.last = 0x3f3f3f3f
        N = len(stones)
        @cache
        def dfs(i, cur, N):
            if i == N:
                self.last = min(self.last, abs(cur))
                return
            # add
            dfs(i + 1, cur + stones[i], N)
            # minus
            dfs(i + 1, cur - stones[i], N)

        dfs(0, 0, N)
        return self.last
