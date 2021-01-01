'''
wrong answer
'''


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pats = list(pattern)
        words = str.split()
        # assert len(pats) == len(words)
        if len(pats) != len(words):
            return False
        
        pats2words = dict(zip(pats, words)) 
        words2pats = dict(zip(words, pats))
        return pats2words == {pat: word for word, pat in words2pats.iteritems()}
        

if __name__ == '__main__':
	pattern = "abba"
	str = "dog cat cat dog"
	assert Solution().wordPattern(pattern, str)
	pattern = "aba"
	str = "cat cat cat dog"
	assert not Solution().wordPattern(pattern, str)

	# wrong answer
	pattern = "abaaba"
	str = "dog cat fish fish cat dog"
	assert not Solution().wordPattern(pattern, str)