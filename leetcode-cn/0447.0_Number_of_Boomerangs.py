'''
Hash Table

执行用时：1248 ms, 在所有 Python3 提交中击败了53.29% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了75.82% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        N = len(points)
        for i in range(N):
            # dist: (x1 - x2) ^ 2 + (y1 - y2) ^2
            dist2cnt = defaultdict(int)
            for j in range(N):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist2cnt[d] += 1
            for d, c in dist2cnt.items():
                ans += c * (c - 1)

        return ans
