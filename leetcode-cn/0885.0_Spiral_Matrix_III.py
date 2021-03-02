'''
approach: Layer by Layer
Time: O(2 * R * 2 * C) = O(R * C)
Space :O(R * C)

执行用时：96 ms, 在所有 Python 提交中击败了7.14%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了42.86%的用户
'''


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        order = []
        idx = 0
        top, left = r0, c0
        bottom, right = r0 + 1, c0 + 1
        while idx < R * C:
            # left to right
            for j in range(left, right + 1):
                if self.withinArea(top, j, R, C):
                    order.append([top, j])
                    idx += 1
            # right to bottom
            for i in range(top + 1, bottom + 1):
                if self.withinArea(i, right, R, C):
                    order.append([i, right])
                    idx += 1
            # right to left
            for j in range(right - 1, left - 1, -1):
                if self.withinArea(bottom, j, R, C):
                    order.append([bottom, j])
                    idx += 1        
            # left to top
            for i in range(bottom, top - 1, -1):
                if self.withinArea(i, left - 1, R, C):
                    order.append([i, left - 1])
                    idx += 1
            top -= 1
            left -= 1
            bottom += 1
            right += 1

        return order
    
    def withinArea(self, i, j, R, C):
        return 0 <= i < R and 0 <= j < C
