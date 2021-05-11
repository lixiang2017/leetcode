'''
You are here!
Your runtime beats 56.95 % of python submissions.
You are here!
Your memory usage beats 54.30 % of python submissions.
'''


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        letters1, letters2 = set(word1), set(word2)
        if letters1 != letters2: return False
        
        count1, count2 = collections.Counter(word1), collections.Counter(word2)
        return sorted(count1.values()) == sorted(count2.values())
