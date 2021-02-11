'''
approach: Heap
Time: O(logN)
Space:O(N)

执行结果：
通过
显示详情
执行用时：248 ms, 在所有 Python 提交中击败了74.21%的用户
内存消耗：17 MB, 在所有 Python 提交中击败了29.56%的用户
'''



import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
