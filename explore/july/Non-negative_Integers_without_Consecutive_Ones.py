'''
124 / 527 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
Last executed input: 94991907
'''
class Solution:
    def findIntegers(self, n: int) -> int:
        # to contruct
        meet = ['']
        i = 0   
        while 1 << (i) <= n:
            next_round = []
            for before in meet:
                if int(before + '0', 2) <= n:
                    next_round.append(before + '0')
                else:
                    break
                if not before or before[-1] == '0':
                    if int(before + '1', 2) <= n:
                        next_round.append(before + '1')    
                    else:
                        break
            meet = next_round
            i += 1
        return len(meet)
        


'''
ref:
https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/solution/jian-dan-zhi-jie-de-fang-fa-by-xfarmer/

You are here!
Your runtime beats 52.56 % of python3 submissions.
You are here!
Your memory usage beats 34.62 % of python3 submissions.
'''
class Solution:
    def findIntegers(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            return 3
        
        nbits = 0
        while n >> nbits:
            nbits += 1
        
        @cache
        def fib(nbits):
            if nbits == 1:
                return 2
            elif nbits == 2:
                return 3
            return fib(nbits - 1) + fib(nbits - 2)

        if n >> (nbits - 2) == 3:
            return fib(nbits)
        else:
            mask = (1 << (nbits - 1)) - 1
            return fib(nbits - 1) + self.findIntegers(n & mask)
