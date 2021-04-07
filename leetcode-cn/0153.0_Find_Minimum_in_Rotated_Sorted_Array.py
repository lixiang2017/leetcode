'''
Time: O(N)
Space: O(1)
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)



'''
Just compare with the right num
approach: Binary Search
Time: O(logN)
Space: O(1)

执行用时：20 ms, 在所有 Python 提交中击败了64.83的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了93.14%的用户
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) / 2
            if nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high = pivot
            
        return nums[low]