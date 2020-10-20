'''
Success
Details
Runtime: 20 ms, faster than 81.94% of Python online submissions for Largest Substring Between Two Equal Characters.
Memory Usage: 13.5 MB, less than 55.07% of Python online submissions for Largest Substring Between Two Equal Characters.
'''

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        import string
        # string.ascii_lowercase
        positions = {c : [] for c in string.ascii_lowercase}
        size = len(s)
        optimal = -1
        for i in xrange(size):
            positions[s[i]].append(i)
        
        for c, p in positions.iteritems():
            if len(p) >= 2:
                optimal = max(optimal, p[-1] - p[0] - 1)
        
        return optimal