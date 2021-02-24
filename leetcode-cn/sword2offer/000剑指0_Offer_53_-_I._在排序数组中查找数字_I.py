'''
approach: Binary Search + Recursion
Time: O(logN + logN) = O(logN)
Space: O(logN), to keep stack.

执行结果：通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了87.84%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了63.66%的用户
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = self.getFirstTarget(nums, target, 0, len(nums) - 1)
        last = self.getLastTarget(nums, target, 0, len(nums) - 1)
        if first != -1 and last != -1:
            return last - first + 1
        else:
            return 0

    def getFirstTarget(self, nums, target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) / 2
        if nums[mid] == target:
            if mid == 0 or (mid > 0 and nums[mid - 1] != target):
                return mid
            else:
                end = mid - 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        return self.getFirstTarget(nums, target, start, end)
    
    def getLastTarget(self, nums, target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) / 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or (mid + 1 < len(nums) and nums[mid + 1] != target):
                return mid
            else:
                start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

        return self.getLastTarget(nums, target, start, end)




'''
approach: Binary Search + Iteration
Time: O(logN + logN) = O(logN)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了72.35%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了89.57%的用户
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = self.getFirstTarget(nums, target, 0, len(nums) - 1)
        last = self.getLastTarget(nums, target, 0, len(nums) - 1)
        if first != -1 and last != -1:
            return last - first + 1
        else:
            return 0

    def getFirstTarget(self, nums, target, start, end):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                if mid == 0 or (mid > 0 and nums[mid - 1] != target):
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
    
    def getLastTarget(self, nums, target, start, end):
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or (mid + 1 < len(nums) and nums[mid + 1] != target):
                    return mid
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
