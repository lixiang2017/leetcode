'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 78.98 % of python submissions.
You are here!
Your memory usage beats 31.25 % of python submissions.
'''


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return 1
                   
        up = None
        wiggle = 1
        for i in range(1, N):
            if nums[i-1] < nums[i]:
                # up
                if up == None:
                    wiggle += 1
                    up = True
                    continue
                if not up:
                    wiggle += 1
                up = True
            elif nums[i-1] > nums[i]:
                # down
                if up == None:
                    wiggle += 1
                    up = False
                    continue
                if up:
                    wiggle += 1
                up = False
        
        return wiggle

'''
Input:
[0,0]
Output:
2
Expected:
1
'''


'''
approach: DP
detect up:
up = down + 1 because previous must be wiggle down
detect down:
down = up + 1

Time: O(N)
Space: O(1)

You are here!
Your runtime beats 94.32 % of python submissions.
You are here!
Your memory usage beats 15.34 % of python submissions.
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 1:
            return 1
        
        # initialize up down because every first numbe can be either up or down
        up = down = 1
        for i in range(1, N):
            # detect up
            if nums[i - 1] < nums[i]:
                up = down + 1
            # detect down
            elif nums[i - 1] > nums[i]:
                down = up + 1
            # if detect equal, do nothing
        return max(up, down)
    

'''
Time: O(N)
Space: O(1)
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        up = down = 1
        for i in range(1, N):
            if nums[i - 1] < nums[i]:
                up = down + 1
            elif nums[i - 1] > nums[i]:
                down = up + 1
        return max(up, down)
    


