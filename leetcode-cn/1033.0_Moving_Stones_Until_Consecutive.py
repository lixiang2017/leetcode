'''
approach: Brainteaser
Time: O(1)
Space: O(1)

执行结果：
通过
显示详情
执行用时：8 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了98.21%的用户

# enumerate answer types
1. sort a, b, c
2. delta1, delta2 = b - a, c - b
3. sort delta1, delta2

(delta1, delta2) -> answer
(1, 1)          -> [0, 0]
(1, delta2)     -> [1, delta2 - 1]
(2, delta2)     -> [1, delta2]    # delta2 >= 2
(delta1, delta2)-> [2, delta1 + delta2 - 2]  # delta1 > 2, delta2 > 2
'''


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        a, b, c = sorted([a, b, c])
        delta1, delta2 = b - a, c - b
        if delta1 > delta2:
            delta1, delta2 = delta2, delta1

        if 1 == delta1 and 1 == delta2:
            return [0, 0]
        elif 1 == delta1:
            return [1, delta2 - 1]
        elif 2 == delta1:
            return [1, delta2]
        else:
            return [2, delta1 + delta2 - 2]
            