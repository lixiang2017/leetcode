'''
Runtime: 73 ms, faster than 20.98% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.9 MB, less than 81.04% of Python3 online submissions for Search Insert Position.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


'''
Runtime: 86 ms, faster than 10.87% of Python3 online submissions for Search Insert Position.
Memory Usage: 15.1 MB, less than 22.59% of Python3 online submissions for Search Insert Position.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
        