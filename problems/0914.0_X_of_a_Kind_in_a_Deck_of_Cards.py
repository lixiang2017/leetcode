'''
Success
Details 
Runtime: 120 ms, faster than 53.02% of Python online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 13.8 MB, less than 60.00% of Python online submissions for X of a Kind in a Deck of Cards.
'''


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        cards = Counter(deck)
        nums = cards.values()
        nums.sort()
        
        for x in range(2, nums[0] + 1):
            if all([num % x == 0 for num in nums]):
                return True
        
        return False
        