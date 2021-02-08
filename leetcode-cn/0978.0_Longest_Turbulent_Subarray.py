'''

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
        