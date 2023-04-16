'''
DFS + cache

Runtime: 2739 ms, faster than 35.80% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
Memory Usage: 242.5 MB, less than 28.79% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
'''
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n, k = len(words), len(words[0]), len(target)
        freq = [[0] * 26 for _ in range(n)]
        MOD = 10 ** 9 + 7
        
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ord(ch) - ord('a')] += 1
        
        @cache
        def cnt(i, j):
            if j >= k:
                return 1
            if i >= n:
                return 0
            idx = ord(target[j]) - ord('a')
            # choose
            c1 = freq[i][idx] * cnt(i + 1, j + 1)
            # not choose
            c2 = cnt(i + 1, j)
            
            return (c1 + c2) % MOD
        
        return cnt(0, 0)


'''
DP

Runtime: 2604 ms, faster than 40.08% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
Memory Usage: 39 MB, less than 70.04% of Python3 online submissions for Number of Ways to Form a Target String Given a Dictionary.
'''
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n, k = len(words), len(words[0]), len(target)
        freq = [[0] * 26 for _ in range(n)]
        MOD = 10 ** 9 + 7
        
        for word in words:
            for i, ch in enumerate(word):
                freq[i][ord(ch) - ord('a')] += 1
        
        f = [[0] * k + [1] for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(k - 1, -1 , -1):
                idx = ord(target[j]) - ord('a')
                f[i][j] = freq[i][idx] * f[i + 1][j + 1] + f[i + 1][j]
                f[i][j] %= MOD

        return f[0][0]
