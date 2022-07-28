'''
执行用时：32 ms, 在所有 Python3 提交中击败了93.67% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.38% 的用户
通过测试用例：253 / 253
'''
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edges = []
        for pp1, pp2 in combinations([p1, p2, p3, p4], 2):
            edges.append((pp1[0] - pp2[0]) * (pp1[0] - pp2[0]) + (pp1[1] - pp2[1]) * (pp1[1] - pp2[1]))
        edges.sort()
        return edges[0] == edges[1] == edges[2] == edges[3] != 0 and edges[4] == edges[5] == 2 * edges[0]
