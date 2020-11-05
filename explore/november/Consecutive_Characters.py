'''
You are here!
Your runtime beats 64.08 % of python submissions.
'''



class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        power = 1
        tmp_power = 1
        size = len(s)
        for i, ch in enumerate(s):
            if i + 1 < size and ch == s[i + 1]:
                tmp_power += 1
                power = max(power, tmp_power)
            else:
                tmp_power = 1
                
        return power
