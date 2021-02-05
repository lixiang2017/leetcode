'''
approach: Two Pointers
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：48 ms, 在所有 Python 提交中击败了49.43%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了67.41%的用户
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        size = len(height)
        left, right = 0, size - 1
        while left < right:
            maximum = max(maximum, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum
