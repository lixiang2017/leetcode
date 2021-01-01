'''
72 / 83 test cases passed.
    Status: Time Limit Exceeded

Submission Result: Time Limit Exceeded 
Last executed input: ["1","2","3","4","6","7","8","9"]
67688637
'''



class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        numbers = 0
        from itertools import permutations, product
        size = len(str(n))
        for i in range(1, size):
            for one in product(digits, repeat=i):
                numbers += 1
        
        for one in product(digits, repeat=size):
            # print 'one: ', one   # one:  (u'7', u'5', u'1')
            if int(''.join(one)) <= n:
                numbers += 1
        
        return numbers


'''
72 / 83 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 1 minute ago
Last executed input: ["1","2","3","4","6","7","8","9"]
67688637
'''

class Solution(object):

    
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        numbers = 0
        from itertools import permutations, product
        choices = len(digits)
        size = len(str(n))
        for i in range(1, size):
            # for one in product(digits, repeat=i):
            numbers += choices ** i
        
        for one in product(digits, repeat=size):
            # print 'one: ', one   # one:  (u'7', u'5', u'1')
            if int(''.join(one)) <= n:
                numbers += 1
        
        return numbers






'''
Run Code Status: Finished
Run Code Result:
Your input

["1","2","3","4","6","7","8","9"]
67688637

Your answer

12255070

Expected answer

12255070
'''

