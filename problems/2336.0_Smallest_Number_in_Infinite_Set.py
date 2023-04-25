'''
Runtime: 150 ms, faster than 40.93% of Python3 online submissions for Smallest Number in Infinite Set.
Memory Usage: 14.5 MB, less than 56.04% of Python3 online submissions for Smallest Number in Infinite Set.
'''
class SmallestInfiniteSet:

    def __init__(self):
        self.popped = []
        # container start index
        self.index = 1
        self.container = []

    def popSmallest(self) -> int:
        if not self.container:
            heappush(self.popped, self.index)
            self.index += 1
            return self.index - 1
        else:
            x = heappop(self.container)
            heappush(self.popped, x)
            return x 

    def addBack(self, num: int) -> None:
        if num in self.popped:
            self.popped.remove(num)
            heappush(self.container, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
