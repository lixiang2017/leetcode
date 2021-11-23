'''
Union Find

Runtime: 3968 ms, faster than 47.90% of Python3 online submissions for Largest Component Size by Common Factor.
Memory Usage: 19.7 MB, less than 91.02% of Python3 online submissions for Largest Component Size by Common Factor.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.p[pj] = pi
            
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UF(max(nums) + 1)
        for i in nums:
            for j in range(2, int(i**0.5) + 1):
                if not i % j:
                    uf.union(i, j)
                    # 下面这一步是必须的，其他数字要依据这个要union在一起。
                    uf.union(i, i // j)
        return max(Counter(uf.find(i) for i in nums).values())
    

'''
1、为数组中每一个数字计算出prime factor list；
2、获得所有prime 的集合；
3、对于每一个数字的prime factor list, 选择第一个factor，其他factor都跟这个factor union;
这一步保证了其他数字有相同factor在之后的操作中会被union在一起。
4、最后看每个数字的第一个factor是属于第几个，其他factor不用管。

Runtime: 5406 ms, faster than 11.38% of Python3 online submissions for Largest Component Size by Common Factor.
Memory Usage: 18.8 MB, less than 94.61% of Python3 online submissions for Largest Component Size by Common Factor.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.p[pj] = pi
            
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        B = []
        for x in nums:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x //= d
                    facs.append(d)
                d += 1
            # the last prime
            # 这个数字可能是1，可能是个质数，
            # 可能是个合数，但经过多轮 //= d 之后变成了个质数。
            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list(set(p for facs in B for p in facs))
        prime2index = {p: i for i, p in enumerate(primes)}
        
        uf = UF(len(primes))
        for facs in B:
            for p in facs:
                uf.union(prime2index[facs[0]], prime2index[p])
        c = Counter(uf.find(prime2index[facs[0]]) for facs in B if facs)
        return max(c.values())


'''
Runtime: 2013 ms, faster than 90.42% of Python3 online submissions for Largest Component Size by Common Factor.
Memory Usage: 17 MB, less than 97.60% of Python3 online submissions for Largest Component Size by Common Factor.
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        
    def find(self, i):
        while i != self.p[i]:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
        return self.p[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.p[pj] = pi
            self.size[pi] += self.size[pj]
            
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        d = {}
        uf = UF(len(nums))
        for i, n in enumerate(nums):
            primes = self.primeFactor(n)
            for p in primes:
                if p in d:
                    uf.union(i, d[p])
                d[p] = i
        return max(uf.size) 
    
    def primeFactor(self, x):
        factors = set()

        while x % 2 == 0:
            x //= 2
            factors.add(2)
        
        for i in range(3, int(sqrt(x)) + 1, 2):
            while x % i == 0:
                factors.add(i)
                x //= i
                
        if x > 2:
            factors.add(x)
        return factors

