'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了63.86%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了21.69%的用户
'''

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = current = 0
        for diff in gain:
            current += diff
            highest = max(highest, current)

        return highest
