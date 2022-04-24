'''
Runtime: 268 ms, faster than 87.68% of Python3 online submissions for Design Skiplist.
Memory Usage: 21 MB, less than 92.89% of Python3 online submissions for Design Skiplist.
'''
class Skiplist:

    def __init__(self):
        self.b = []

    def search(self, target: int) -> bool:
        idx = bisect_left(self.b, target)
        return idx < len(self.b) and target == self.b[idx]

    def add(self, num: int) -> None:
        bisect.insort(self.b, num)

    def erase(self, num: int) -> bool:
        idx = bisect_left(self.b, num)
        if not (idx < len(self.b) and num == self.b[idx]):
            return False
        self.b = self.b[: idx] + self.b[idx + 1: ]
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
