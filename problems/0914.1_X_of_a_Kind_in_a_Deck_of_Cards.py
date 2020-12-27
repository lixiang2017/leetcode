'''
Success
Details 
Runtime: 124 ms, faster than 34.88% of Python online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 13.5 MB, less than 96.28% of Python online submissions for X of a Kind in a Deck of Cards.
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
        size = len(deck)
        nums.sort()
        
        for x in range(2, nums[0] + 1):
            if size % x == 0:
                if all([num % x == 0 for num in nums]):
                    return True

        return False
        