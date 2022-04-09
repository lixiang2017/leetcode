'''
heap

Runtime: 189 ms, faster than 23.36% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.3 MB, less than 31.19% of Python3 online submissions for Kth Largest Element in a Stream.
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # min heap for size == k, keep more large nums in heap
        self.h = nums
        heapify(self.h)
        self.k = k
        while len(self.h) > k:
            heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)
        while len(self.h) > self.k:
            heappop(self.h)
        return self.h[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
