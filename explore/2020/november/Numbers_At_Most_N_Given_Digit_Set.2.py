'''
You are here!
Your runtime beats 47.06 % of python submissions.
'''


class Solution(object):
    
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        numbers = 0

        choices = len(digits)
        size = len(str(n))
        for i in range(1, size):
            numbers += choices ** i
        
        for i in range(size):  # firstly, from high postion of the given N
            hasSameNum = False
            for digit in digits:
                if int(digit) < int(str(n)[i]):
                    numbers += choices ** (size - i - 1)
                elif int(digit) == int(str(n)[i]):
                    hasSameNum = True
            
            if not hasSameNum:
                return numbers
            
        return numbers + 1
            