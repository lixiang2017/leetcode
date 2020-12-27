'''
approach: Greatest Common Divisor, GCD

Success
Details 
Runtime: 124 ms, faster than 34.88% of Python online submissions for X of a Kind in a Deck of Cards.
Memory Usage: 13.8 MB, less than 60.00% of Python online submissions for X of a Kind in a Deck of Cards.

ref:
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/
'''

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
        