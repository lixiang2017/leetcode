'''
Success
Details
Runtime: 44 ms, faster than 59.19% of Python online submissions for Shuffle String.
Memory Usage: 13.7 MB, less than 15.24% of Python online submissions for Shuffle String.
'''

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        size = len(s)
        shuffled = ['a'] * size
        for i in xrange(size):
            # s[i]
            # indices[i]
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)
