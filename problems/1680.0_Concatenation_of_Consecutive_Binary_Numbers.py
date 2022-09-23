'''
simulation + bit shift
T: O(N)
S: O(1)

Runtime: 3168 ms, faster than 37.01% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 13.9 MB, less than 62.20% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # bit len 
        b = 0
        MOD = 10 ** 9 + 7
        ans = 0
        i = 0
        while i <= n:
            if (1 << b) <= i:
                b += 1
            ans <<= b 
            ans += i
            ans %= MOD
            i += 1
        return ans 

'''
Runtime: 1195 ms, faster than 96.06% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
Memory Usage: 14 MB, less than 62.20% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # bit len 
        b = ans = i = 0
        MOD = 10 ** 9 + 7
        while i <= n:
            if (1 << b) <= i:
                b += 1
            ans = ((ans << b) + i) % MOD 
            i += 1
        return ans 
        