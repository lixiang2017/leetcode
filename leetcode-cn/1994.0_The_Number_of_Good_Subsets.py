'''
执行用时：460 ms, 在所有 Python3 提交中击败了27.91% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了37.21% 的用户
通过测试用例：91 / 91
'''
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        good_nums = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        MOD = 10 ** 9 + 7
        c = Counter(nums)
        prime_dict = defaultdict(int)
        for gn in good_nums:
            for i, p in enumerate(primes):
                if gn % p == 0:
                    prime_dict[gn] |= 1 << i 
        
        dp = [1] + [0] * ((1 << len(primes)) - 1)
        for gn in good_nums[1: ]:
            for j in range(len(dp)):
                if prime_dict[gn] & j == 0:
                    dp[prime_dict[gn] | j] += c[gn] * dp[j]
                    dp[prime_dict[gn] | j] %= MOD
        
        return (1 << c[1]) * sum(dp[1: ]) % MOD 
        

