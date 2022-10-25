'''
Runtime: 53 ms, faster than 67.17% of Python3 online submissions for Check If Two String Arrays are Equivalent.
Memory Usage: 13.8 MB, less than 98.50% of Python3 online submissions for Check If Two String Arrays are Equivalent.
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        