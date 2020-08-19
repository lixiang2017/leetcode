'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3429/
You are here!
Your runtime beats 71.46 % of python submissions.
99 / 99 test cases passed.
    Status: Accepted
Runtime: 20 ms
Memory Usage: 12.9 MB
    
Submitted: 0 minutes ago
'''


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = [word + 'ma' if word[0] in vowels else word[1:] + word[0] + 'ma' for word in words]
        for i in xrange(len(words)):
            words[i] += 'a' * (i + 1)
        return ' '.join(words)



if __name__ == '__main__':
    S = "I speak Goat Latin"
    ans = "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
    assert Solution().toGoatLatin(S) == ans


    S = "The quick brown fox jumped over the lazy dog"
    ans = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    assert Solution().toGoatLatin(S) == ans
