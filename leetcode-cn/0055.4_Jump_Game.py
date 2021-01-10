'''
Approach: Greedy

Success
Details 
Runtime: 68 ms, faster than 63.41% of Python online submissions for Jump Game.
Memory Usage: 15.2 MB, less than 80.68% of Python online submissions for Jump Game.

ref:
https://leetcode.com/problems/jump-game/solution/
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        lastPos = size - 1
        
        for i in range(size - 2, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        
        return lastPos == 0
        
        