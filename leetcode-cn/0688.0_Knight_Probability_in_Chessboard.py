'''
BFS

执行用时：224 ms, 在所有 Python3 提交中击败了68.09% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了97.16% 的用户
通过测试用例：22 / 22
'''
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        prob = defaultdict(float)
        prob[(row, column)] = 1.0

        dirs = [(-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1)]
        for _ in range(k):
            next_p = defaultdict(float)
            for r, c in prob:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < n and 0 <= nc < n:
                        next_p[(nr, nc)] += prob[(r, c)] / 8 
            prob = next_p
        
        return sum(prob.values())

