'''
Success
Details 
Runtime: 16 ms, faster than 71.38% of Python online submissions for Word Pattern.
Memory Usage: 13.6 MB, less than 45.50% of Python online submissions for Word Pattern.
'''


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        size = len(pattern)
        words = s.split()
        if len(words) != size: return False
        
        bijection = {}
        word2letter = {}
        for letter, word in zip(pattern, words):
            if letter in bijection:
                if bijection[letter] != word:
                    return False
            else:
                bijection[letter] = word
            
            if word in word2letter:
                if word2letter[word] != letter:
                    return False
            else:
                word2letter[word] = letter
        
        return True

'''
Input
"abba"
"dog dog dog dog"
Output
true
Expected
false
'''

'''
Input
"abba"
"dog dog dog dog"
Output
true
Expected
false
'''

