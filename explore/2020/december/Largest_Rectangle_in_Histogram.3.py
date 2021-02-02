'''
Time: O(N^2) with pruning and primming

You are here!
Your runtime beats 6.94 % of python submissions.
You are here!
Your memory usage beats 37.92 % of python submissions.
'''


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        size = len(heights)
        largest = 0
        
        for i in range(size):
            minHeight = heights[i]
            # print 'minHeight: ', minHeight
            if i + 1 < size and heights[i] <= heights[i + 1]:  # cut branches
                continue
            for j in range(i, -1, -1):
                minHeight = min(heights[j], minHeight)
                largest = max(largest, (i - j + 1) * minHeight)
                # print largest
        return largest

