'''
approach: Two Pointers
Time: O(N * k), where N is the number of words in d and k is the length of string s.
Space: O(1)

You are here!
Your runtime beats 60.25 % of python submissions.
You are here!
Your memory usage beats 89.44 % of python submissions.
'''


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longest = ''
        for word in d:
            if self.isSubsequence(word, s):
                if len(longest) < len(word):
                    longest = word
                elif len(longest) == len(word):
                    longest = min(longest, word)
        return longest
        
    
    def isSubsequence(self, x, y):
        '''
        check whether x is substring of y
        '''
        j = 0
        for i in range(len(y)):
            if j < len(x) and x[j] == y[i]:
                j += 1
        return j == len(x)



'''
You are here!
Your runtime beats 26.71 % of python submissions.
You are here!
Your memory usage beats 28.57 % of python submissions.
'''


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longest = ''
        for word in d:
            # if self.isSubsequence(word, s):
            if self.isSubstring(word, s):
                if len(longest) < len(word):
                    longest = word
                elif len(longest) == len(word):
                    longest = min(longest, word)
        return longest
        
    
    def isSubsequence(self, x, y):
        '''
        check whether x is substring of y
        '''
        j = 0
        for i in range(len(y)):
            if j < len(x) and x[j] == y[i]:
                j += 1
        return j == len(x)
        
    
    def isSubstring(self, a, b):
        '''
        check whether a is substring of b
        '''
        indexa = indexb = 0
        while indexa < len(a) and indexb < len(b):
            if a[indexa] == b[indexb]:
                indexa += 1
            indexb += 1
        return indexa == len(a)
    
    