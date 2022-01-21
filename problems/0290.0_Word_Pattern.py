'''
Approach: Two Hash Maps

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


'''
Runtime: 52 ms, faster than 11.80% of Python3 online submissions for Word Pattern.
Memory Usage: 14.3 MB, less than 55.31% of Python3 online submissions for Word Pattern.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split()
        if len(words) != n:
            return False
        p2s, s2p = dict(), dict()
        for pp, ss in zip(pattern, words):
            if pp not in p2s and ss not in s2p:
                p2s[pp] = ss
                s2p[ss] = pp
            elif pp in p2s and ss in s2p:
                if p2s[pp] != ss or s2p[ss] != pp:
                    return False
                else:
                    continue
            else:
                return False
        return True



