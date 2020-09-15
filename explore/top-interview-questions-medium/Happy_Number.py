'''
You are here!
Your runtime beats 96.07 % of python submissions.
'''



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = []
        while True:
            sum = 0
            for char in str(n):
                digit = int(char)
                sum += digit * digit
                
            if sum == 1:
                return True
            elif sum in seen:
                return False
            else:
                seen.append(sum)
        
            n = sum