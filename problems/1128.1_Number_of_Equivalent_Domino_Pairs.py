'''
Success
Details
Runtime: 192 ms, faster than 94.40% of Python online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 25.5 MB, less than 13.60% of Python online submissions for Number of Equivalent Domino Pairs.
'''


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        hashmap = collections.defaultdict(int)
        
        for a, b in dominoes:
            if a > b:
                a, b = b, a

            hashmap[(a, b)] += 1
                
        pairs = 0
        for count in hashmap.itervalues():
            # if count > 1:  # can be removed/primmed
            pairs += count * (count - 1) / 2
        return pairs
    