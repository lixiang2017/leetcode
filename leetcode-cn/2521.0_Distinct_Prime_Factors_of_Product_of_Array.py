'''
执行用时：104 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = set()
        nums = set(nums)
        for x in nums:
            for i in range(2, x + 1):
                if x % i == 0:
                    f.add(i)
                    while x % i == 0:
                        x //= i
                    if x < i:
                        break
        return len(f)

'''
埃氏筛

执行用时：108 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：81 / 81
'''
MX = 1000 + 1
primes = []
is_prime = [True] * MX 
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = set()
        nums = set(nums)
        for x in nums:
            for p in primes:
                if x % p == 0:
                    f.add(p)
        return len(f)


'''
欧拉筛

执行用时：144 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了0.00% 的用户
通过测试用例：81 / 81
'''
MX = 1000 + 1
primes = []
is_prime = [True] * MX 
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i * p >= MX:
            break
        is_prime[i * p] = False
        if i % p == 0:
            break

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = set()
        nums = set(nums)
        for x in nums:
            for p in primes:
                if x % p == 0:
                    f.add(p)
        return len(f)


'''
while i * i <= x 还是比 for i in range(2, x + 1) 快不少。

执行用时：48 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了0.00% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        f = set()
        nums = set(nums)
        for x in nums:
            i = 2
            while i * i <= x:
                if x % i == 0:
                    f.add(i)
                    while x % i == 0:
                        x //= i
                i += 1
            if x > 1:
                f.add(x)
        return len(f)

