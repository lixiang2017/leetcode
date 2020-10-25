'''
Success
Details 
Runtime: 28 ms, faster than 100.00% of Python online submissions for Slowest Key.
Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Slowest Key.
'''


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        # store duration in releaseTimes list to save space
        releaseTimes = [releaseTimes[0]] + [y - x for x, y in zip(releaseTimes, releaseTimes[1: ])]
        return max(zip(releaseTimes, keysPressed))[1]