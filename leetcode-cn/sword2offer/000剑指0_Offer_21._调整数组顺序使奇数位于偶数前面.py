'''
approach: Two Pointers (Head & Tail)
# 首尾双指针
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：36 ms, 在所有 Python 提交中击败了80.61%的用户
内存消耗：18.1 MB, 在所有 Python 提交中击败了83.82%的用户
'''

class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        left, right = 0, size - 1
        
        while left < right:
            # 
            if (nums[left] & 1):
                left += 1
                continue
            elif not(nums[right] & 1):
                right -= 1
                continue
            else: # swap left and right
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums
