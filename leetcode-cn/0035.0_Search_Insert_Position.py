'''
Binary Search,T:O(logN),S:O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了41.26% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了26.78% 的用户
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        l, r = 0, N
        #print(nums, target)
        idx = 0
        while l <= r:
            mid = (r - l) // 2 + l
            #print(r, l)
            if mid >= N:
                return N
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                idx = mid
                r = mid - 1
            else:
                idx = mid + 1
                l = mid + 1
        
        return idx



'''
Sort,T:O(NlogN)

执行用时：36 ms, 在所有 Python3 提交中击败了84.91% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了16.88%
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        nums.append(target)
        nums.sort()
        return nums.index(target)
