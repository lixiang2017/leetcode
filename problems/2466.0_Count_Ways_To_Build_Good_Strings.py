'''
DFS + cache

Runtime: 3607 ms, faster than 5.51% of Python3 online submissions for Count Ways To Build Good Strings.
Memory Usage: 787.4 MB, less than 5.51% of Python3 online submissions for Count Ways To Build Good Strings.
'''
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def ways(length):
            if length == 0:
                return 1
            if length <= 0:
                return 0
            return ways(length - zero) + ways(length - one)
        
        ans = 0
        for l in range(low, high + 1):
            ans += ways(l)
            ans %= MOD
        return ans 
        
'''
DP

Runtime: 265 ms, faster than 72.44% of Python3 online submissions for Count Ways To Build Good Strings.
Memory Usage: 21 MB, less than 65.35% of Python3 online submissions for Count Ways To Build Good Strings.
'''
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        f = [1] + [0] * high
        for i in range(high - min(zero, one) + 1):
            f[i] %= MOD
            if i + zero <= high:
                f[i + zero] += f[i]
            if i + one <= high:
                f[i + one] += f[i]
                
        return sum(f[low: high + 1]) % MOD
        

'''
Runtime: 249 ms, faster than 81.10% of Python3 online submissions for Count Ways To Build Good Strings.
Memory Usage: 20.9 MB, less than 70.87% of Python3 online submissions for Count Ways To Build Good Strings.
'''
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        f = [1] + [0] * high
        for i in range(high - min(zero, one) + 1):
            f[i] %= MOD
            if i + zero <= high:
                f[i + zero] += f[i]
            if i + one <= high:
                f[i + one] += f[i]
                
        return sum(f[low: ]) % MOD
        
