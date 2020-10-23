'''
Success
Details
Runtime: 188 ms, faster than 98.40% of Python online submissions for Number of Equivalent Domino Pairs.
Memory Usage: 25.2 MB, less than 13.60% of Python online submissions for Number of Equivalent Domino Pairs.
'''

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        
        # for domino in dominoes:
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            # if [a, b] in hashmap:  # TypeError: unhashable type: 'list'
            if (a, b) in hashmap:   # use tuple instead
                hashmap[(a, b)] += 1
            else:
                hashmap[(a, b)] = 1
                
        # 2 --> 1
        # 3 --> 3
        # 4 --> 3 + 2 + 1
        pairs = 0
        for _, count in hashmap.iteritems():
            if count > 1:
                pairs += count * (count - 1) / 2
        return pairs
    
    
'''
TypeError: unhashable type: 'list'
    if [a, b] in hashmap:
Line 13 in numEquivDominoPairs (Solution.py)
    ret = Solution().numEquivDominoPairs(param_1)
Line 46 in _driver (Solution.py)
    _driver()
Line 56 in <module> (Solution.py)
'''
        