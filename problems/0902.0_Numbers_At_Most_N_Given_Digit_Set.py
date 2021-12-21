'''
Runtime: 32 ms, faster than 62.96% of Python3 online submissions for Numbers At Most N Given Digit Set.
Memory Usage: 14.3 MB, less than 50.93% of Python3 online submissions for Numbers At Most N Given Digit Set.
'''
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        cnt = 0
        D = len(digits)
        L = len(str(n))
        for i in range(1, L):
            cnt += D ** i
        
        for i in range(L):
            hasSameNum = False
            for digit in digits:
                if int(digit) < int(str(n)[i]):
                    cnt += D ** (L - 1 - i)
                elif int(digit) == int(str(n)[i]):
                    hasSameNum = True  
            if not hasSameNum:
                return cnt
        return cnt + 1
        