'''
approach: Hash Table
Time: O(N)
Space: O(1)

You are here!
Your memory usage beats 57.89 % of python submissions.
'''



from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = Counter(s)
        digitsCnt = [0] * 10
        # 
        memos = [('z', 'zero', 0),  # first round
           ('w', 'two', 2),
           ('u', 'four', 4),
           ('x', 'six', 6),
           ('g', 'eight', 8),
           ('o', 'one', 1),   # second round
           ('h', 'three', 3),
           ('f', 'five', 5),
           ('s', 'seven', 7),
           ('i', 'nine', 9)]   # third round
        for distinct, word, digit in memos:
            distinctCnt = letters[distinct]
            if distinctCnt > 0:
                digitsCnt[digit] += distinctCnt
                for ch in word:
                    letters[ch] -= distinctCnt
    
        return ''.join([str(digit) * cnt for digit, cnt in enumerate(digitsCnt) if cnt > 0])
        