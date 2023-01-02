'''
Sieve of Eratosthenes
埃式筛预处理 + bisect_left

执行用时：1284 ms, 在所有 Python3 提交中击败了77.85% 的用户
内存消耗：66.5 MB, 在所有 Python3 提交中击败了41.33% 的用户
通过测试用例：66 / 66
'''
MX = 5 * 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False  

class Solution:
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)


'''
欧拉筛预处理 + bisect_left

执行用时：1620 ms, 在所有 Python3 提交中击败了77.30% 的用户
内存消耗：66.4 MB, 在所有 Python3 提交中击败了42.50% 的用户
通过测试用例：66 / 66
'''
MX = 5 * 10 ** 6 + 1
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
    def countPrimes(self, n: int) -> int:
        return bisect_left(primes, n)

'''
埃式筛

执行用时：3160 ms, 在所有 Python3 提交中击败了56.63% 的用户
内存消耗：66.3 MB, 在所有 Python3 提交中击败了44.85% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        MX = n
        primes = []
        is_prime = [True] * MX
        for i in range(2, MX):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, MX, i):
                    is_prime[j] = False
        return len(primes)


'''
欧拉筛

执行用时：4996 ms, 在所有 Python3 提交中击败了27.75% 的用户
内存消耗：66.4 MB, 在所有 Python3 提交中击败了44.11% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        MX = n
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
        return len(primes)



