'''
Euler's sieve
线性筛（欧拉筛）
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Euler's_sieve

https://leetcode.cn/problems/closest-prime-numbers-in-range/solution/yu-chu-li-zhi-shu-mei-ju-by-endlesscheng-uw2b/
https://leetcode.cn/problems/closest-prime-numbers-in-range/

思路：
    每个合数只被划掉一次
    被它的最小质因子划掉

The time complexity of this algorithm is O(n).
'''

MX = 10 ** 6 + 1
primes = []
is_prime = [True] * MX
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
    for p in primes:
        if i * p >= MX:
            break
        is_prime[i * p] = False
        # 将重复筛选剔除
        if i % p == 0:
            break 

print(f'There are {len(primes)} primes from 2 through {MX}.')
print('Top 30 primes are: ')
print(primes[: 30])

'''
There are 78498 primes from 2 through 1000001.
Top 30 primes are: 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
'''