'''
Approach: One Hash Map

Success
Details 
Runtime: 12 ms, faster than 91.19% of Python online submissions for Word Pattern.
Memory Usage: 13.5 MB, less than 45.50% of Python online submissions for Word Pattern.
'''


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words): return False
        
        bijection = {}
        for letter, word in zip(pattern, words):
            if letter not in bijection:
                if word in bijection.values():
                    return False
                else:
                    bijection[letter] = word
            elif bijection[letter] != word:
                return False
        
        return True
        
        