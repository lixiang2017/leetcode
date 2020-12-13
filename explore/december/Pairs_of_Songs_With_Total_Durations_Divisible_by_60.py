'''
You are here!
Your runtime beats 98.35 % of python submissions.
'''

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        pairs = 0
        time = [t % 60 for t in time]
        count = [0 for _ in range(60)]
        for t in time:
            count[t] += 1
        
        pairs += count[0] * (count[0] - 1) / 2
        pairs += count[30] * (count[30] - 1) / 2
        for i in range(1, 30):
            pairs += count[i] * count[60 - i]
        
        return pairs
    