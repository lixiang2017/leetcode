'''
DP
from left to right

Runtime: 496 ms, faster than 66.35% of Python3 online submissions for Jump Game.
Memory Usage: 15.4 MB, less than 35.35% of Python3 online submissions for Jump Game.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        farmost = nums[0]
        for i, x in enumerate(nums):
            if i > farmost:
                break
            else:
                farmost = max(farmost, i + x)
                if farmost >= N - 1:
                    return True
        return False


'''
Runtime: 819 ms, faster than 23.15% of Python3 online submissions for Jump Game.
Memory Usage: 15.4 MB, less than 11.93% of Python3 online submissions for Jump Game.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        farmost = nums[0]
        for i, x in enumerate(nums):
            if i > farmost:
                return False
            else:
                farmost = max(farmost, i + x)
                if farmost >= N - 1:
                    return True


'''
Runtime: 460 ms, faster than 40.29% of Python online submissions for Jump Game.
Memory Usage: 14.6 MB, less than 25.06% of Python online submissions for Jump Game.
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(lambda m, (i, x): max(m, i + x) * (i <= m), enumerate(nums, 1), 1) > 0
        



'''
Using parentheses to unpack the arguments in a lambda is not allowed in Python3. See PEP 3113 for the reason why.
https://stackoverflow.com/questions/15712210/python-3-2-lambda-syntax-error

Runtime: 544 ms, faster than 43.94% of Python3 online submissions for Jump Game.
Memory Usage: 15.4 MB, less than 35.35% of Python3 online submissions for Jump Game.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return reduce(lambda m, ix: max(m, ix[0] + ix[1]) * (ix[0] <= m), enumerate(nums, 1), 1) > 0


'''
go backwards
假设可以到达末尾，再从末尾反推。

Runtime: 476 ms, faster than 80.55% of Python3 online submissions for Jump Game.
Memory Usage: 15.4 MB, less than 11.93% of Python3 online submissions for Jump Game.
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        lastPos = size - 1
        for i in range(size - 2, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        
        return not lastPos