'''
21 / 21 个通过测试用例
状态：通过
执行用时: 1312 ms
内存消耗: 34.6 MB
提交时间：21 分钟前
'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        L = len(self.nums)
        if L % 2:
            return self.nums[L // 2]
        else:
            return (self.nums[L // 2 - 1] + self.nums[L // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''
max heapq + min heapq

执行用时：392 ms, 在所有 Python3 提交中击败了57.43% 的用户
内存消耗：34.5 MB, 在所有 Python3 提交中击败了42.56% 的用户
通过测试用例：21 / 21
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if not self.minh or num > self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)
        #  adjust
        L1, L2 = len(self.minh), len(self.maxh)
        if L1 >= L2 + 2:
            n = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -n)
        if L2 >= L1 + 2:
            n = -heapq.heappop(self.maxh)
            heapq.heappush(self.minh, n)

    def findMedian(self) -> float:
        L1, L2 = len(self.minh), len(self.maxh)
        if L1 > L2:
            return self.minh[0]
        elif L1 < L2:
            return -self.maxh[0]
        else:
            return (self.minh[0] - self.maxh[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

