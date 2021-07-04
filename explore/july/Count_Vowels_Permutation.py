'''
BFS + Hash Table
T: O(N)
S: O(1)

You are here!
Your runtime beats 12.37 % of python3 submissions.
You are here!
Your memory usage beats 50.26 % of python3 submissions.
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        follow = {
            'a': ('e'),
            'e': ('a', 'i'),
            'i': ('a', 'e', 'o', 'u'),
            'o': ('i', 'u'),
            'u': ('a'),
        }
        
        # q = deque(['a', 'e', 'i', 'o', 'u'])
        c = Counter(['a', 'e', 'i', 'o', 'u'])
        while n > 1:
            tries = Counter()
            for ch, times in c.items():
                for next_ch in follow[ch]:
                    tries[next_ch] += times
            
            # c = tries
            c = {ch: times % MOD for ch, times in tries.items()}
            n -= 1
            
        return sum(c.values()) % MOD


'''
DP + List
T: O(N)
S: O(1)

You are here!
Your runtime beats 45.36 % of python3 submissions.
You are here!
Your memory usage beats 64.18 % of python3 submissions.
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        '''
        a, e, i, o, u
        0, 1, 2, 3, 4
        '''
        MOD = 10 ** 9 + 7
        rules = [
            [1],
            [0, 2],
            [0, 1, 3, 4],
            [2, 4],
            [0]
        ]
        dp = [1] * 5
        for _ in range(n - 1):
            curr_dp = [0] * 5
            for i in range(5):
                for next_ch in rules[i]:
                    curr_dp[next_ch] += dp[i] % MOD
            
            dp = curr_dp
        
        return sum(dp) % MOD


'''
DP 
T: O(N)
S: O(1)

You are here!
Your runtime beats 90.46 % of python3 submissions.
You are here!
Your memory usage beats 97.16 % of python3 submissions.
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i % MOD, (i + o) % MOD
        
        return (a + e + i + o + u) % MOD
