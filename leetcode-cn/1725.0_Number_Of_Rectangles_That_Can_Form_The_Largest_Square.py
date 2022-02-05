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


'''
T: O(N)
S: O(1)

执行用时：56 ms, 在所有 Python3 提交中击败了13.44% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了50.54% 的用户
通过测试用例：68 / 68
'''
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        maxl = 0
        for l, w in rectangles:
            sqr = min(l, w)
            if sqr > maxl:
                ans = 1
                maxl = sqr
            elif sqr == maxl:
                ans += 1
        return ans 

