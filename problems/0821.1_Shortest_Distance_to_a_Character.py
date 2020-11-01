'''
Success
Details 
Runtime: 28 ms, faster than 77.89% of Python online submissions for Shortest Distance to a Character.
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
        size = len(positions)
        j = 0
        for i, ch in enumerate(S):
            # shortest.append(min(abs(position - i) for position in positions))
            pos1 = positions[j]
            if j + 1 < size:
                pos2 = positions[j + 1]
            else:
                pos2 = float('-inf')
            dist1 = abs(pos1 - i)
            dist2 = abs(pos2 - i)
            if dist1 < dist2:
                shortest.append(dist1)
            else:
                shortest.append(dist2)
                j += 1
        
        return shortest
        