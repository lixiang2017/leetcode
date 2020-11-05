'''
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)

Success
Details 
Runtime: 60 ms, faster than 98.51% of Python online submissions for Count Unique Characters of All Substrings of a Given String.
Memory Usage: 13.6 MB, less than 26.87% of Python online submissions for Count Unique Characters of All Substrings of a Given String.
'''


class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        
        res = 0
        for i, c in enumerate(s):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = j, i
        
        for c, [k, j] in index.iteritems():
            res += (len(s) - j) * (j - k)
        return res % (10 ** 9 + 7)
        