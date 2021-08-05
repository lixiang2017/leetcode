'''
DP,T:O(N^2),S:O(N^2)
博弈论

You are here!
Your runtime beats 49.43 % of python3 submissions.
You are here!
Your memory usage beats 43.82 % of python3 submissions.
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0] * N for _ in range(N)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] -dp[i][j - 1])
                
        return dp[0][N - 1] > 0


'''
DP,T:O(N^2),S:O(N^2)
博弈论

You are here!
Your runtime beats 51.72 % of python3 submissions.
You are here!
Your memory usage beats 91.36 % of python3 submissions.
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = copy.copy(piles)
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
        
        return dp[N - 1] > 0

'''
T:O(1),S:O(1)
博弈论

You are here!
Your runtime beats 80.62 % of python3 submissions.

'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
