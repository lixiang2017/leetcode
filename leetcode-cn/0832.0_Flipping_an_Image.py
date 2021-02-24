'''
Time: O(N ^ 2)
Space: O(1)

执行结果：
通过
显示详情
执行用时：44 ms, 在所有 Python 提交中击败了23.56%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了19.47%的用户
'''

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 - pixel for pixel in row[::-1]] for row in A]


'''
执行结果：
通过
显示详情
执行用时：40 ms, 在所有 Python 提交中击败了45.55%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了69.47%的用户
'''


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ pixel for pixel in row[::-1]] for row in A]
