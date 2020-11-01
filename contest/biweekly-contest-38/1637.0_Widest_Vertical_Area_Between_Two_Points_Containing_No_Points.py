'''
52 / 52 test cases passed.
Status: Accepted
Runtime: 736 ms
Memory Usage: 57.2 MB
Submitted: 2 minutes ago
'''



class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        xs = set()
        for x, y in points:
            xs.add(x)
        
        xs = sorted(list(xs))
        widest = 0
        size = len(xs)
        for i in range(size - 1):
            if xs[i + 1] - xs[i] > widest:
                widest = xs[i + 1] - xs[i]
        
        return widest
    