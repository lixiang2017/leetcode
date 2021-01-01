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
        
        pats2words = {}
        for i in xrange(len(pats)):
            print pats2words
            if pats[i] in pats2words and words[i] not in pats2words.values():
                if pats2words[pats[i]] == words[i]:
                    continue
                else:
                    return False
            elif pats[i] in pats2words and words[i] in pats2words.values():
                return False
            else:
                pats2words[pats[i]] = words[i]

        return True
        

if __name__ == '__main__':
    pattern = "abba"
    str = "dog cat cat dog"
    assert Solution().wordPattern(pattern, str)
    pattern = "aba"
    str = "cat cat cat dog"
    assert not Solution().wordPattern(pattern, str)

    pattern = "abaaba"
    str = "dog cat fish fish cat dog"
    assert not Solution().wordPattern(pattern, str)

    pattern = "abba"
    str = "dog dog dog dog"
    assert not Solution().wordPattern(pattern, str)