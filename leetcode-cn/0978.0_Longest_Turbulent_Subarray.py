'''
approach: Dynamic Programming
Time: O(N)
Space: O(N)

执行结果：
通过
显示详情
执行用时：112 ms, 在所有 Python 提交中击败了78.05%的用户
内存消耗：16.1 MB, 在所有 Python 提交中击败了36.88%的用户
'''


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest = 1
        size = len(arr)
        up = [1] * size
        down = [1] * size
        for i in range(1, size):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
            elif arr[i - 1] > arr[i]:
                down[i] = up[i - 1] + 1
            longest = max(longest, up[i], down[i])
        
        return longest
