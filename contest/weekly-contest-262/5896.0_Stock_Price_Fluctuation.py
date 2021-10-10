'''
17 / 17 个通过测试用例
状态：通过
执行用时: 880 ms
内存消耗: 56.1 MB
提交时间：11 小时前
'''
class StockPrice:

    def __init__(self):
        # prices
        self.ps = []
        # price -> cnt
        self.cnt = defaultdict(int)
        self.maxh = []
        self.minh = []

    def update(self, timestamp: int, price: int) -> None:
        t, p = timestamp, price
        i = bisect.bisect_left(self.ps, [t, 0])
        if i == len(self.ps):
            self.ps.append([t, p])
            self.cnt[p] += 1
            heappush(self.maxh, -p)
            heappush(self.minh, p)
            return
        
        if t == self.ps[i][0]:
            oldp = self.ps[i][1]
            self.cnt[oldp] -= 1
            while self.maxh and 0 == self.cnt[-self.maxh[0]]:
                heappop(self.maxh)
            while self.minh and 0 == self.cnt[self.minh[0]]:
                heappop(self.minh)
            self.ps[i][1] = p
            self.cnt[p] += 1
            heappush(self.maxh, -p)
            heappush(self.minh, p)
        else:
            bisect.insort(self.ps, [t, p], i, i + 1)
            heappush(self.maxh, -p)
            heappush(self.minh, p)  
            self.cnt[p] += 1

    def current(self) -> int:
        return self.ps[-1][1]

    def maximum(self) -> int:
        return -self.maxh[0]

    def minimum(self) -> int:
        return self.minh[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

