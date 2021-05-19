'''
approach: Heap
Time: O(Nlogk)
Space: O(k)

执行用时：48 ms, 在所有 Python3 提交中击败了70.56% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了50.11% 的用户
'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            if len(queue) < k:
                heapq.heappush(queue, num)
            elif num > queue[0]:
                heapq.heapreplace(queue, num)
        
        return queue[0]