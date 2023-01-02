'''
埃式筛
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

The time complexity of this algorithm is O(n log log n).
'''

MX = 10 ** 6 + 1
primes = []
is_prime = [True] * MX 
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False 

print(f'There are {len(primes)} primes from 2 through {MX}.')
print('Top 30 primes are: ')
print(primes[: 30])


'''
There are 78498 primes from 2 through 1000001.
Top 30 primes are: 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
'''