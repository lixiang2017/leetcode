'''
use the no-adjacent-flowers rule
Time: O(n)
Space: O(1)

You are here!
Your runtime beats 100.00 % of python submissions.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n <= 0: return True
        
        index = 0
        while index < len(flowerbed):
            if flowerbed[index]:
                index += 2
            else:
                if index < len(flowerbed) - 1 and flowerbed[index + 1]:
                    index += 3
                else:
                    n -= 1
                    index += 2
                    if n <= 0: return True
        
        return n <= 0