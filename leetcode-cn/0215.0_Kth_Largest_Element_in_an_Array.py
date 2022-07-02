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


'''
quick select
T: O(N)
S: O(logN)

执行用时：40 ms, 在所有 Python3 提交中击败了83.59% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了76.71% 的用户
通过测试用例：32 / 32
'''
class Helper:

    @staticmethod
    def partition(nums: List[int], l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    @staticmethod
    def randomPartition(nums: List[int], l: int, r: int) -> int:
        idx = randint(l, r)
        nums[idx], nums[r] = nums[r], nums[idx]
        return Helper.partition(nums, l, r)

    @staticmethod
    def quickSelected(nums: List[int], l: int, r: int, k: int) -> int:
        index = Helper.randomPartition(nums, l, r)
        if index == k:
            return nums[k]
        elif index < k:
            return Helper.quickSelected(nums, index + 1, r, k)
        else:
            return Helper.quickSelected(nums, l, index - 1, k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return Helper.quickSelected(nums, 0, len(nums) - 1, len(nums) - k)



