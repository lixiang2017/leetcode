'''
执行用时：880 ms, 在所有 Python3 提交中击败了26.70% 的用户
内存消耗：53.6 MB, 在所有 Python3 提交中击败了25.65% 的用户
通过测试用例：18 / 18
'''
from sortedcontainers import SortedDict

class StockPrice:

    def __init__(self):
        # for update, current
        self.time2price = SortedDict()
        # for max, min
        self.price_cnt = SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time2price:
            # remove old price
            p = self.time2price[timestamp]
            self.price_cnt[p] -= 1
            if 0 == self.price_cnt[p]:
                self.price_cnt.pop(p)
                
        # add new price
        if price in self.price_cnt:
            self.price_cnt[price] += 1
        else:
            self.price_cnt[price] = 1
        self.time2price[timestamp] = price

    def current(self) -> int:
        return self.time2price.peekitem(index=-1)[1]

    def maximum(self) -> int:
        return self.price_cnt.peekitem(index=-1)[0]

    def minimum(self) -> int:
        return self.price_cnt.peekitem(index=0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
