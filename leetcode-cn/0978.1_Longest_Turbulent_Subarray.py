'''
approach: Dynamic Programming
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：108 ms, 在所有 Python 提交中击败了82.93%的用户
内存消耗：15.3 MB, 在所有 Python 提交中击败了90.98%的用户
'''


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest = 1
        size = len(arr)
        up = down = 1
        for i in range(1, size):
            if arr[i - 1] < arr[i]:
                up = down + 1
                down = 1
            elif arr[i - 1] > arr[i]:
                down = up + 1
                up = 1
            else:
                down = 1
                up = 1
            longest = max(longest, up, down)
        
        return longest
