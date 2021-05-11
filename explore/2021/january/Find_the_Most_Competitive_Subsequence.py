'''
approach: Mono Increasing Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 39.64 % of python submissions.
You are here!
Your memory usage beats 85.71 % of python submissions.
'''


class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        stack = []
        size = len(nums)
        for i in range(size):
            while stack and stack[-1] > nums[i] and len(stack) + size - i > k:
                stack.pop(-1)
            stack.append(nums[i])
        
        return stack[: k]
