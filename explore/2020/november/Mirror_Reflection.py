'''
You are here!
Your runtime beats 98.48 % of python submissions.
'''


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while (p % 2 == 0 and q % 2 == 0):
            p /= 2
            q /= 2
        
        # 4 : 1
        if p % 2 == 0:
            return 2
        # 3 : 2
        if q % 2 == 0:
            return 0
        # 3 : 1
        return 1