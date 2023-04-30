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



'''
执行用时：44 ms, 在所有 Python3 提交中击败了16.85% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.43% 的用户
通过测试用例：187 / 187
'''
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if a + 2 == c:
            minimum_moves = 0
        elif b - a <= 2 or c - b <= 2:
            minimum_moves = 1
        else:
            minimum_moves = 2
        maxmum_moves = (c - b - 1) + (b - a - 1)
        return [minimum_moves, maxmum_moves]

        