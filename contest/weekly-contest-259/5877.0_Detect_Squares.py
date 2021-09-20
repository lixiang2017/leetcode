'''
AC
'''
class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x = defaultdict(set)
        self.y = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[tuple(point)] += 1
        self.x[x].add(y)
        self.y[y].add(x)

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        ans = 0
        for x in self.y[y0]:
            if x != x0:
                for y in [y0 + (x - x0), y0 - (x - x0)]:    # 别忘了另一个方向！！！
                    if y in self.x[x0] and (x, y) in self.points:
                        a, b, c, d = self.points[(x, y0)], 1, self.points[(x, y)], self.points[(x0, y)]
                        #print(a, b, c, d)
                        ans += a * b * c * d
        
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
