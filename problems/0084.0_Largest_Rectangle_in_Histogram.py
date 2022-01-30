'''
Runtime: 880 ms, faster than 55.92% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 28.2 MB, less than 35.74% of Python3 online submissions for Largest Rectangle in Histogram.
'''
'''idx     0  1  2  3  4  5
heights = [2, 1, 5, 6, 2, 3]
left    = [-1,-1,1, 2, 1, 4]
right   = [1, 6, 4, 4, 6, 6]

'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        lessFromLeft, lessFromRight = [0] * n, [0] * n
        lessFromLeft[0] = -1
        lessFromRight[-1]= n
        # to find position/index
        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p
        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p
        for i in range(n):
            maxArea = max(maxArea, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
        return maxArea
