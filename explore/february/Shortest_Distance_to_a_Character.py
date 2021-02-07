'''
Time: O(N + N + N) = O(N)
Space: O(N + N + N) = O(N)

You are here!
Your runtime beats 80.50 % of python submissions.
You are here!
Your memory usage beats 96.50 % of python submissions.
'''

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        size = len(s)
        directer = [size for _ in range(size)]
        reverser = [size for _ in range(size)]
        
        nearest = -1
        for i in range(size):
            if s[i] == c:
                nearest = i
            if nearest != -1:
                directer[i] = i - nearest
        
        nearest = -1
        for i in range(size - 1, -1, -1):
            if s[i] == c:
                nearest = i
            if nearest != -1:
                reverser[i] = nearest - i
        
        return [min(d, r) for d, r in zip(directer, reverser)]
