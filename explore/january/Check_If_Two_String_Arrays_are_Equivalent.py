'''
You are here!
Your runtime beats 69.53 % of python submissions.
You are here!
Your memory usage beats 82.76 % of python submissions.
'''


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)
