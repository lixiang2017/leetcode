'''
approach: Greedy
Time: O(N)
Space: O(1)

执行结果：通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了99.41%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了17.65%的用户
'''

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = number = 0
        for l, w in rectangles:
            side = min(l, w)
            if side == maxLen:
                number += 1
            elif side > maxLen:
                maxLen = side
                number = 1
        return number
                