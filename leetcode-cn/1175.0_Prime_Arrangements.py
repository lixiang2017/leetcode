'''

执行用时：40 ms, 在所有 Python3 提交中击败了53.82% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.61% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # prime count
        p_cnt = 0

        def isPrime(i):
            for j in range(2, i):
                if i % j == 0:
                    return False 
            return True

        for i in range(2, n + 1):
            if isPrime(i):
                p_cnt += 1

        ans, MOD = 1, 10 ** 9 + 7
        for i in range(2, p_cnt + 1):
            ans *= i 
            ans %= MOD 
        for i in range(2, n - p_cnt + 1):
            ans *= i 
            ans %= MOD 
        return ans         



'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.71% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.93% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # prime count
        p_cnt = 0

        def isPrime(i):
            return all(i % j != 0 for j in range(2, i))

        for i in range(2, n + 1):
            if isPrime(i):
                p_cnt += 1

        ans, MOD = 1, 10 ** 9 + 7
        for i in range(2, p_cnt + 1):
            ans *= i 
            ans %= MOD 
        for i in range(2, n - p_cnt + 1):
            ans *= i 
            ans %= MOD 
        return ans         


'''
执行用时：40 ms, 在所有 Python3 提交中击败了53.82% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.19% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(i):
            return all(i % j != 0 for j in range(2, i))

        # prime count
        p_cnt = sum(isPrime(i) for i in range(2, n + 1))
        MOD = 10 ** 9 + 7
        return reduce(operator.mul, chain(range(2,  p_cnt + 1), range(2, n - p_cnt + 1)), 1) % MOD 

'''
执行用时：44 ms, 在所有 Python3 提交中击败了20.48% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了67.07% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isPrime(i):
            return all(i % j != 0 for j in range(2, i))

        # prime count
        p_cnt = sum(isPrime(i) for i in range(2, n + 1))
        MOD = 10 ** 9 + 7
        return reduce(lambda x, y: x * y % MOD, 
            chain(range(2,  p_cnt + 1), range(2, n - p_cnt + 1)), 
            1)

