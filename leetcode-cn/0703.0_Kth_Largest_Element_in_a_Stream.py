'''
approach: Heap
Time: O(logN)
Space: O(N)

执行结果：通过
显示详情
执行用时：
264 ms, 在所有 Python 提交中击败了46.54%的用户
内存消耗：17.2 MB, 在所有 Python 提交中击败了13.84%的用户
'''



import heapq 

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) > k:
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
