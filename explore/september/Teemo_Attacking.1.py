'''
do not use the length of timeSeries, remember the last attack time

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
        if not timeSeries or not duration:
            return 0
        
        total_time = 0
        last_attack = -1
        for time in timeSeries:
            if last_attack == -1:
                last_attack = time
                continue
            else:
                total_time += min(duration, time - last_attack)
                last_attack = time
        
        return total_time + duration
                
            