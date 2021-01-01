'''
You are here!
Your runtime beats 90.91 % of python submissions.
'''

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total_time = 0
        attacks = len(timeSeries)
        if attacks == 0:
            return 0
        elif attacks == 1:
            return duration
        
        for i in range(attacks - 1):
            if timeSeries[i + 1] - timeSeries[i] > duration:
                total_time += duration
            else:
                total_time += timeSeries[i + 1] - timeSeries[i]
        
        return total_time + duration


