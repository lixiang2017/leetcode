'''
approach: Sieve of Eratosthenes
Time: O(NloglogN), https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
Space: O(N)

You are here!
Your runtime beats 29.38 % of python3 submissions.
You are here!
Your memory usage beats 36.58 % of python3 submissions.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if not isPrime[i]:
                i += 1
                continue
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i    
            i += 1
        
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
        