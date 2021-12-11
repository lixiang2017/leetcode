'''
45 / 70 test cases passed.
    Status: Memory Limit Exceeded
    
Submitted: 9 minutes ago
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        if a > b:
            a, b = b, a
        if b % a == 0:
            return a * n % MOD
        ai = bi = 1
        h = []
        ans = 0
        seen = set()
        while n:
            ax, bx = ai * a, bi * b
            ax, bx = ax % MOD, bx % MOD
            if ax <= bx:
                if ax not in seen:
                    heappush(h, ax)
                    seen.add(ax)
                    ans = ax
                    n -= 1
                ai += 1
            else:
                if bx not in seen:
                    heappush(h, bx)
                    seen.add(bx)
                    ans = bx
                    n -= 1
                bi += 1
                
        return ans


'''
容斥原理

Runtime: 87 ms, faster than 17.17% of Python3 online submissions for Nth Magical Number.
Memory Usage: 14.4 MB, less than 31.31% of Python3 online submissions for Nth Magical Number.
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        from math import gcd
        MOD = 10**9 + 7
        # least common multiple
        l = a // gcd(a, b) * b
        # count 0 to l
        m = l // a + l // b - 1
        q, r = divmod(n, m)
        if r == 0:
            return q * l % MOD
        
        head = [a, b]
        for _ in range(r - 1):
            if head[0] <= head[1]:
                head[0] += a
            else:
                head[1] += b
        return (q * l + min(head)) % MOD

'''
Runtime: 81 ms, faster than 18.18% of Python3 online submissions for Nth Magical Number.
Memory Usage: 14.3 MB, less than 59.60% of Python3 online submissions for Nth Magical Number.
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # from math import gcd
        def gcd(x, y):
            if x == 0:
                return y
            return gcd(y % x, x)
        
        MOD = 10**9 + 7
        # least common multiple
        l = a // gcd(a, b) * b
        # count 0 to l
        m = l // a + l // b - 1
        q, r = divmod(n, m)
        if r == 0:
            return q * l % MOD
        
        head = [a, b]
        for _ in range(r - 1):
            if head[0] <= head[1]:
                head[0] += a
            else:
                head[1] += b
        return (q * l + min(head)) % MOD


'''
Runtime: 31 ms, faster than 72.73% of Python3 online submissions for Nth Magical Number.
Memory Usage: 14.1 MB, less than 92.93% of Python3 online submissions for Nth Magical Number.
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            if x == 0:
                return y
            return gcd(y % x, x)
        
        MOD = 10**9 + 7
        # least common multiple of a and b
        l = a // gcd(a, b) * b
        
        def magic_below_x(x):
            # how many magical numbers are <= x?
            return x // a + x // b - x // l
        
        lo, hi = 0, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            if magic_below_x(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % MOD
