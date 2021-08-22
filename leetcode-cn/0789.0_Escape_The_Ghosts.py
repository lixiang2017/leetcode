'''
曼哈顿距离
dist(A, B) = abs(Ai - Bi) + abs(Aj - Bj)
Time: O(N)
Space: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了63.38% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.98% 的用户
'''
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        t = abs(target[0]) + abs(target[1])
        # nearest ghost, the length of path between ghost and target
        nearest = float('inf')
        for g in ghosts:
            nearest = min(nearest, abs(g[0] - target[0]) + abs(g[1] - target[1]))
        return t < nearest
