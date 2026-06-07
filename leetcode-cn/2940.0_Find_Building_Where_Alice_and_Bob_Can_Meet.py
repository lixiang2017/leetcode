class SegmentTree:
    def __init__(self, a: list[int]):
        n = len(a)
        self.max = [0] * (2 << (n - 1).bit_length())
        self.build(a, 1, 0, n - 1)

    def maintain(self, o: int):
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])
    
    def build(self, a: list[int], o: int, l: int, r: int):
        if l == r:
            self.max[o] = a[l]
            return 
        m = (l + r) // 2
        self.build(a, o * 2, l, m)
        self.build(a, o * 2 + 1, m + 1, r)
        self.maintain(o)

    def find_first(self, o: int, l: int, r: int, L: int, v: int) -> int:
        if self.max[o] <= v:
            return -1

        if l == r:
            return l
        m = (l + r) // 2
        if L <= m and (pos := self.find_first(o * 2, l, m, L, v)) >= 0:
            return pos
        return self.find_first(o * 2 + 1, m + 1, r, L, v)
        
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        t = SegmentTree(heights)
        n = len(heights)
        for a, b in queries:
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans.append(b)
            else:
                i = t.find_first(1, 0, n - 1, b + 1, heights[a])
                ans.append(i)
        return ans
    


