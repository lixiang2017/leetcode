'''
approach: DP + Greedy
Time: O(N + N + N) = O(N)
Space: O(N + N) = O(N)

执行用时：28 ms, 在所有 Python 提交中击败了58.23%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了26.58%的用户
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        leftHeight = [0] * N
        rightHeight = [0] * N
        volume = 0
        leftmax = rightmax = -sys.maxint
        for i in range(N):
            leftmax = max(leftmax, height[i])
            leftHeight[i] = leftmax
        for i in range(N - 1, -1, -1):
            rightmax = max(rightmax, height[i])
            rightHeight[i] = rightmax
        
        for i in range(N):
            if height[i] < min(leftHeight[i], rightHeight[i]):
                volume += (min(leftHeight[i], rightHeight[i]) - height[i])

        return volume
