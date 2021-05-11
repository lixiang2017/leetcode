'''
approach: Iteration
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 60.47 % of python3 submissions.
You are here!
Your memory usage beats 89.39 % of python3 submissions.
'''

class Solution:
    def fib(self, n: int) -> int:
        sequence = [0] * (n + 5)
        sequence[1] = 1
        i = 2 
        while i <= n:
            sequence[i] = sequence[i - 2] + sequence[i - 1]
            i += 1
        return sequence[n]
