'''
backtracking

72 / 75 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True
            
            furthestJump = min(position + nums[position], len(nums) - 1)
            for nextPosition in range(position + 1, furthestJump + 1):
                if canJumpFromPosition(nextPosition, nums):
                    return True
            
            return False
        
        return canJumpFromPosition(0, nums)
        

'''
backtracking

72 / 75 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True
            
            furthestJump = min(position + nums[position], len(nums) - 1)
            # for nextPosition in range(position + 1, furthestJump + 1):
            for nextPosition in range(furthestJump, position, -1):
                if canJumpFromPosition(nextPosition, nums):
                    return True
            
            return False
        
        return canJumpFromPosition(0, nums)


'''
Dynamic Programming Top-down

74 / 75 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[25000...

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
        # -1 for unknown
        # 0 for bad
        # 1 for good
        memo = [-1 for _ in range(size)]
        memo[-1] = 1
        
        def canJumpFromPosition(position, nums):
            # if position == len(nums) - 1:
            if memo[position] != -1:
                return True if memo[position] == 1 else False
            
            furthestJump = min(position + nums[position], len(nums) - 1)
            # for nextPosition in range(position + 1, furthestJump + 1):
            for nextPosition in range(furthestJump, position, -1):
                if canJumpFromPosition(nextPosition, nums):
                    memo[position] = 1
                    return True
            
            memo[position] = 0
            return False
        
        return canJumpFromPosition(0, nums)
        
        
'''
Dynamic Programming Bottom-up

74 / 75 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[25000...

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
        # -1 for unknown
        # 0 for bad
        # 1 for good
        memo = [-1 for _ in range(size)]
        memo[-1] = 1
        
        for i in range(size - 2, -1, -1):
            furthestJump = min(i + nums[i], size - 1)

            for nextPosition in range(i + 1, furthestJump + 1):
                
                if memo[nextPosition] == 1:
                    memo[i] = 1
                    break
        
        return memo[0] == 1
        
        