'''
Success
Details 
Runtime: 60 ms, faster than 27.14% of Python online submissions for Shortest Distance to a Character.
Memory Usage: 13.7 MB, less than 40.20% of Python online submissions for Shortest Distance to a Character.
'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        positions = []
        for i, ch in enumerate(S):
            if ch == C:
                positions.append(i)
        
        shortest = []
        for i, ch in enumerate(S):
            shortest.append(min(abs(position - i) for position in positions))
        
        return shortest
    