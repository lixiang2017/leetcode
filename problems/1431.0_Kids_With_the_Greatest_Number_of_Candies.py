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
    

'''
Runtime: 34 ms, faster than 90.72% of Python3 online submissions for Kids With the Greatest Number of Candies.
Memory Usage: 13.8 MB, less than 50.96% of Python3 online submissions for Kids With the Greatest Number of Candies.
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [x + extraCandies >= m for x in candies]
        