'''
Brute Force
Time: O(N ^ 2)
Space:O(1)

执行结果：
超出时间限制
显示详情
最后执行的输入：
[1454,2249,4922,5151,7349,1022,8655,8124,2157,2303,5213,3217,437...
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maximum = 0
        size = len(height)
        for i in range(size - 1):
            for j in range(i + 1, size):
                maximum = max(maximum, min(height[i], height[j]) * (j - i))
        return maximum
