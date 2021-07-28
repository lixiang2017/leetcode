'''

You are here!
Your runtime beats 75.71 % of python3 submissions.
You are here!
Your memory usage beats 27.14 % of python3 submissions.
'''
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # hash table, N to beautiful array
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                memo[N] = [2 * x - 1 for x in f((N + 1) // 2)] + [2 * x for x in f(N // 2)]
            return memo[N]
        return f(n)
