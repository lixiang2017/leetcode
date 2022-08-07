'''
DP
T: O(N)
S: O(1)

Runtime: 136 ms, faster than 95.76% of Python3 online submissions for Count Vowels Permutation.
Memory Usage: 13.8 MB, less than 93.55% of Python3 online submissions for Count Vowels Permutation.
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a
        return (a + e + i + o + u) % MOD 
