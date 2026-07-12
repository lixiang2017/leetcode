"""
hash table + sort

执行用时：100 ms, 在所有 Python3 提交中击败了37.62% 的用户
内存消耗：38.3 MB, 在所有 Python3 提交中击败了5.28% 的用户
通过测试用例：38 / 38
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        c = Counter(arr)
        s = sorted(c)
        rank = dict()
        r = 1
        for x in s:
            rank[x] = r
            r += 1
        return list(map(rank.__getitem__, arr))


"""
执行用时：84 ms, 在所有 Python3 提交中击败了68.98% 的用户
内存消耗：33.2 MB, 在所有 Python3 提交中击败了49.84% 的用户
通过测试用例：38 / 38
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        rank = {x: r for r, x in enumerate(s, 1)}
        return list(map(rank.__getitem__, arr))


"""
执行用时：80 ms, 在所有 Python3 提交中击败了80.53% 的用户
内存消耗：33 MB, 在所有 Python3 提交中击败了78.55% 的用户
通过测试用例：38 / 38
"""


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        rank = {x: r for r, x in enumerate(s, 1)}
        return [rank[x] for x in arr]


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pair = [(x, i) for i, x in enumerate(arr)]
        pair.sort()
        ans = [1] * len(arr)
        for p1, p2 in pairwise(pair):
            x1, idx1 = p1
            x2, idx2 = p2
            if x1 == x2:
                ans[idx2] = ans[idx1]
            else:
                ans[idx2] = ans[idx1] + 1
        return ans 
