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


'''
Runtime: 41 ms, faster than 61.10% of Python3 online submissions for Word Pattern.
Memory Usage: 13.8 MB, less than 74.33% of Python3 online submissions for Word Pattern.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for p, w in zip(pattern, words):
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p 
            elif p in p2w and w in w2p:
                if w != p2w[p] or p != w2p[w]:
                    return False
            else:
                return False
        return True
        
'''
Wrong Answer
Details
Input
"aba"
"cat cat cat dog"
Output
true
Expected
false

Wrong Answer
Details
Input
"aba"
"dog cat cat"
Output
true
Expected
false
'''


'''
Runtime: 28 ms, faster than 94.22% of Python3 online submissions for Word Pattern.
Memory Usage: 13.8 MB, less than 99.08% of Python3 online submissions for Word Pattern.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern = list(pattern)
        return list(map(words.index, words)) == list(map(pattern.index, pattern))

'''
Runtime: 29 ms, faster than 91.56% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 74.33% of Python3 online submissions for Word Pattern.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len(s.split()) and len(set(pattern)) == len(set(s.split())) == len(set(zip(pattern, s.split())))
 
