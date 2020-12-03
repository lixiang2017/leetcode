'''
Success
Details 
Runtime: 12 ms, faster than 91.19% of Python online submissions for Word Pattern.
Memory Usage: 13.8 MB, less than 5.14% of Python online submissions for Word Pattern.
'''

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        pattern = list(pattern)
        
        return map(words.index, words) == map(pattern.index, pattern)
        
        