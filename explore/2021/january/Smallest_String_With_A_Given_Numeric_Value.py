'''
approach: Greedy + DFS


93 / 93 test cases passed.
Status: Accepted
Runtime: 1204 ms
Memory Usage: 92.6 MB

You are here!
Your runtime beats 19.61 % of python submissions.
'''


'''
from string import ascii_letters, ascii_lowercase, ascii_uppercase
'''

from string import ascii_lowercase

class Solution(object):
    letters = {ord(ch) - ord('a') + 1: ch for ch in ascii_lowercase}
    
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k <= 0 or n <= 0:
            return ''
        
        if k > n + 24:
            last_letter = 'z'
            return self.getSmallestString(n - 1, k - 26) + last_letter            
        else:
            last_letter = self.letters[k - (n - 1)]
            leading = 'a' * (n - 1)
            return leading + last_letter
