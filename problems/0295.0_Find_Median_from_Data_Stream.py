'''
min heap + max heap

Runtime: 1193 ms, faster than 65.00% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 36.2 MB, less than 32.61% of Python3 online submissions for Find Median from Data Stream.
'''
class MedianFinder:

    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        if self.minh and num >= self.minh[0]:
            heappush(self.minh, num)
        else:
            heappush(self.maxh, -num)
        while len(self.minh) - len(self.maxh) >= 2:
            heappush(self.maxh, -heappop(self.minh))
        while len(self.maxh) - len(self.minh) >= 2:
            heappush(self.minh, -heappop(self.maxh))

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0]) / 2
        elif len(self.minh) + 1 == len(self.maxh):
            return -self.maxh[0]
        else:
            return self.minh[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
