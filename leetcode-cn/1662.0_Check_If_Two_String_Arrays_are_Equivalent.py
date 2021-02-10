'''
执行结果：通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了33.47%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了57.52%的用户
'''

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)
