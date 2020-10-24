'''
You are here!
Your runtime beats 97.40 % of python submissions.
'''


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        
        min_left = [nums[0], ]
        for i in range(1, size):
            min_left.append(min(min_left[i - 1], nums[i]))
        
        stack = []
        
        for j in range(size - 1, -1, -1):
            if nums[j] > min_left[j]:
                while stack and stack[-1] <= min_left[j]:
                    # stack.pop(-1)
                    stack.pop()
                
                if stack and nums[j] > stack[-1]: #  > min_left[j]:  # useless
                    print nums[j], stack[-1], min_left[j]
                    return True
                # else:  # Wrong
                stack.append(nums[j])
                    
        return False
        