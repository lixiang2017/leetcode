'''
执行用时：72 ms, 在所有 Python3 提交中击败了90.70% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了49.37% 的用户
通过测试用例：10 / 10
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapify(self.h)
        while len(self.h) > k:
            heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) == self.k:
            heappushpop(self.h, val)
        else:
            heappush(self.h, val)
        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
