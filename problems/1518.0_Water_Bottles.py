'''
Success
Details 
Runtime: 16 ms, faster than 77.97% of Python online submissions for Water Bottles.
Memory Usage: 13.4 MB, less than 6.09% of Python online submissions for Water Bottles.
'''

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drink = numBottles
        empty = numBottles
        while empty >= numExchange:
            full = empty / numExchange
            empty = empty % numExchange
            drink += full
            empty += full
        
        return drink
        