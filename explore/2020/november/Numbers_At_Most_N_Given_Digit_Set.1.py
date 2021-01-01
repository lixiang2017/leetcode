'''
63 / 83 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
Last executed input: ["1","2","3","4","5","6","7","8"]
8363065
'''




class Solution(object):

    numbers = 0
    
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
          
        self.dfs([], digits, n)
        
        return self.numbers
        
    def dfs(self, init, digits, n):
        if len(init) > len(str(n)):
            return 
        
        if init and len(init) < len(str(n)):
            self.numbers += 1 
        elif init:
            one = int(''.join(init))
            if one <= n:
                self.numbers += 1

        for digit in digits:
            self.dfs(init + [digit], digits, n)
