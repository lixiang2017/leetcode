'''
Approach: Greedy
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了98.48%的用户
内存消耗：
14.6 MB, 在所有 Python 提交中击败了42.45%的用户
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

            rightmost = max(rightmost, i + nums[i])
            if rightmost >= size - 1:
                return True
        
        return False
