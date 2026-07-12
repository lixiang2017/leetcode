class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        uf = UF(n)
        i = j = 0
        while i <= j and j < n:
            while j < n and nums[j] - nums[i] <= maxDiff:
                uf.union(i, j)
                j += 1
            i += 1
        return [uf.is_connected(u, v) for u, v in queries]


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        idx = [i for i, (x, y) in enumerate(pairwise(nums)) if y - x > maxDiff]
        return [bisect_left(idx, u) == bisect_left(idx, v) for u, v in queries]
    

class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        id = list(accumulate([y - x > maxDiff for (x, y) in pairwise(nums)], initial=0))
        return [id[u] == id[v] for u, v in queries]
