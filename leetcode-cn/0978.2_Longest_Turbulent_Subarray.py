'''
approach: Sliding Window / Two Pointers
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：
104 ms, 在所有 Python 提交中击败了85.37%的用户
内存消耗：15.3 MB, 在所有 Python 提交中击败了90.98%的用户
'''


class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest = 0
        size = len(arr)
        if size < 2:
            return size

        left, right = 0, 1
        pre = False
        while right < size:
            current =  arr[right - 1] < arr[right]
            if (pre == current):
                left = right - 1
            if arr[right - 1] == arr[right]:
                left = right
            right += 1
            longest = max(longest, right - left)
            pre = current

        return longest
