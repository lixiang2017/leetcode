'''
Success
Details
Runtime: 20 ms, faster than 81.94% of Python online submissions for Largest Substring Between Two Equal Characters.
Memory Usage: 13.6 MB, less than 55.07% of Python online submissions for Largest Substring Between Two Equal Characters.
'''

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        optimal = -1
        
        position = defaultdict(list)
        for i, c in enumerate(s):
            position[c].append(i)
        
        for indices in position.values():
            # optimal = max(optimal, max(indices) - min(indices) - 1)  # also ok
            optimal = max(optimal, indices[-1] - indices[0] - 1)
        
        return optimal