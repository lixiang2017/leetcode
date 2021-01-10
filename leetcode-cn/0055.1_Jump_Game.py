'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了79.14%的用户
内存消耗：
14.7 MB, 在所有 Python 提交中击败了30.64%的用户
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        rightmost = 0

        for i in range(size):
            if rightmost < i:
                break
            if rightmost == i and 0 == nums[i]:
                break
                
            rightmost = max(rightmost, i + nums[i])
        
        return rightmost >= size - 1
