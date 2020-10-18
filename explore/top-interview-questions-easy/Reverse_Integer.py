'''
You are here!
Your runtime beats 49.06 % of python submissions.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # isNegative = True if x < 0 else False
        if x < 0:
            isNegative = True
            x = -x
        else:
            isNegative = False
        
        digits = []
        while x:
            digits.append(x % 10)
            x /= 10
        
        print 'digits: ', digits
        reverse_x = 0
        for digit in digits:
            reverse_x *= 10
            reverse_x += digit
        
        if isNegative:
            reverse_x = - reverse_x
            
        # return reverse_x
        
        # overflow   
        if reverse_x > 2 ** 31 - 1 or reverse_x < - 2 ** 31:
            return 0
        else:
            return reverse_x
 
        '''
        Submission Result: Wrong Answer 
        Input: 1534236469
        Output: 9646324351
        Expected: 0
        Stdout: digits:  [9, 6, 4, 6, 3, 2, 4, 3, 5, 1]
        '''
