'''
Runtime: 75 ms, faster than 30.47% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 15 MB, less than 48.15% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)



'''
Runtime: 86 ms, faster than 18.98% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 14.9 MB, less than 48.15% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                if r > 0 and nums[r] >= nums[r - 1]:
                    r -= 1
                else:
                    return nums[r]

        return nums[l]
        