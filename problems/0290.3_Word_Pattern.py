'''
Approach: Single Index Hash Map

https://leetcode.com/problems/word-pattern/solution/

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
        words = s.split()
        if len(pattern) != len(words): return False
        
        bijection = {}
        for i in range(len(words)):
            c = pattern[i]
            w = words[i]
            
            char_key = 'char_{}'.format(c)
            char_word = 'word_{}'.format(w)
            
            if char_key not in bijection:
                bijection[char_key] = i
                
            if char_word not in bijection:
                bijection[char_word] = i
            
            if bijection[char_key] != bijection[char_word]:
                return False
        
        return True
        
        
'''
Implementation

Differentiating between character and string: In Python there is no separate char type. And for cases such as:

pattern: 'abba'
s: 'b a a b'
Using the same hash map will not work properly. A workaround is to prefix each character in pattern with "char_" and each word in s with "word_".

'''