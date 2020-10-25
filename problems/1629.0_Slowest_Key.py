'''
Success
Details 
Runtime: 44 ms, faster than 50.00% of Python online submissions for Slowest Key.
Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Slowest Key.
'''


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        longest, key = releaseTimes[0], keysPressed[0]
        size = len(releaseTimes)
        for i in range(1, size):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > longest or (duration == longest and keysPressed[i] > key):
                longest = duration
                key = keysPressed[i]

        return key