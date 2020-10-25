'''
Success
Details
Runtime: 28 ms, faster than 50.82% of Python online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.3 MB, less than 11.91% of Python online submissions for Kids With the Greatest Number of Candies.
'''


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        if not candies:
            return []
        
        maximum = max(candies)
        greatest = []
        for candy in candies:
            greatest.append(True if candy + extraCandies >= maximum else False)
        
        return greatest


'''
Success
Details
Runtime: 24 ms, faster than 76.79% of Python online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.3 MB, less than 11.91% of Python online submissions for Kids With the Greatest Number of Candies.
'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        return [True if candy + extraCandies >= max(candies) else False for candy in candies]
    

