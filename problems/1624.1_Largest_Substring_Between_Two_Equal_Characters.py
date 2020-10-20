'''
Success
Details
Runtime: 16 ms, faster than 92.07% of Python online submissions for Largest Substring Between Two Equal Characters.
Memory Usage: 13.5 MB, less than 55.07% of Python online submissions for Largest Substring Between Two Equal Characters.
'''

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        optimal = -1
        
        position = {}
        for i, c in enumerate(s):
            if c in position:
                optimal = max(optimal, i - position[c] - 1)
            else:
                position[c] = i

        return optimal
