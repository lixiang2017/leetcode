'''
approach: Sliding Window
Time: O(N)
Space:O(1)

执行结果：
通过
显示详情
执行用时：148 ms, 在所有 Python 提交中击败了5.17%的用户
内存消耗：20 MB, 在所有 Python 提交中击败了29.31%的用户
'''


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total = sum(cardPoints)
        size = len(cardPoints)
        width = size - k
        if 0 == width: return total
        i = 0
        minPoints = currentPoints = 0
        while i < width:
            currentPoints += cardPoints[i]
            i += 1

        minPoints = currentPoints
        while i < size:
            currentPoints = currentPoints + cardPoints[i] - cardPoints[i - width]
            minPoints = min(minPoints, currentPoints)
            i += 1

        return total - minPoints
        