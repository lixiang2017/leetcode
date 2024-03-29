'''
Binary Search
T: O(logN)
S: O(1)

Runtime: 407 ms, faster than 9.79% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 28.19% of Python3 online submissions for Binary Search.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

'''
Binary Search
T: O(logN)
S: O(1)

Runtime: 268 ms, faster than 74.92% of Python3 online submissions for Binary Search.
Memory Usage: 15.4 MB, less than 77.82% of Python3 online submissions for Binary Search.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
