'''
hash table

执行用时：220 ms, 在所有 Python3 提交中击败了64.56% 的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了15.19% 的用户
通过测试用例：54 / 54
'''
class DetectSquares:

    def __init__(self):
        self.points_cnt = defaultdict(int)
        self.xs = set()
        self.ys = set()

    def add(self, point: List[int]) -> None:
        self.points_cnt[tuple(point)] += 1
        x, y = point
        self.xs.add(x)
        self.ys.add(y)

    def count(self, point: List[int]) -> int:
        ans = 0    
        xp, yp = point
        for x in self.xs:
            if x == xp:
                continue
            edge = abs(x - xp)
            for y in [yp + edge, yp - edge]:
                if y in self.ys and (xp, y) in self.points_cnt and (x, yp) in self.points_cnt\
                        and (x, y) in self.points_cnt:
                    ans += self.points_cnt[(xp, y)] * self.points_cnt[(x, yp)] * self.points_cnt[(x, y)]

        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
