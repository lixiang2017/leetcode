'''
approach: Brainteaser
Time: O(1)
Space: O(1)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了74.42%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了87.06%的用户
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        sizeA, sizeB = len(a), len(b)
        if sizeA != sizeB:
            return max(sizeA, sizeB)
        else:
            return sizeA if a != b else -1



'''
执行用时：32 ms, 在所有 Python3 提交中击败了75.26% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了46.09% 的用户
通过测试用例：40 / 40
'''
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))