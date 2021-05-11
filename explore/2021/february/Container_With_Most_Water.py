'''
approach: Greedy + Two Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 45.25 % of python submissions.
You are here!
Your memory usage beats 43.01 % of python submissions.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maximum = 0
        while left < right:
            width = right - left
            shorter = min(height[left], height[right])
            maximum = max(maximum, width * shorter)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum
    