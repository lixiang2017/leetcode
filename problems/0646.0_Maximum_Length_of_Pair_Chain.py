'''
Accepted	1574 ms	16.7 MB	python3
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                # i -> j
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
