'''
520. Detect Capital
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3409/

550 / 550 test cases passed.
    Status: Accepted
Runtime: 8 ms
Memory Usage: 12.6 MB
    
You are here!
Your runtime beats 100.00 % of python submissions.
'''

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        if 1 == len(word):
            return True
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True

        return False
        

if __name__ == '__main__':
    word = "USA"
    assert Solution().detectCapitalUse(word)

    word = "leetcode"
    assert Solution().detectCapitalUse(word)

    word = "Google"
    assert Solution().detectCapitalUse(word)

    word = "FlaG"
    assert not Solution().detectCapitalUse(word)    

    word = "G"
    assert Solution().detectCapitalUse(word)

    word = "g"
    assert Solution().detectCapitalUse(word)