'''

You are here!
Your runtime beats 29.46 % of python3 submissions.
You are here!
Your memory usage beats 63.79 % of python3 submissions.
'''
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        

    def findMedian(self) -> float:
        N = len(self.arr)
        if N % 2:
            return self.arr[N // 2]
        else:
            return (self.arr[N // 2 - 1] + self.arr[N // 2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()