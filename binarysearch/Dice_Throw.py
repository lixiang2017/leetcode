'''
DFS + memo

Success!
Your code took 288 milliseconds — faster than 69.00% in Python
'''
class Solution:
    MOD = 10 ** 9 + 7
    @cache
    def solve(self, n, faces, total):
        if total <= 0 or (n * faces < total) or n == 0:
            return 0
        if n == 1 and total <= faces:
            return 1
        ans = 0
        for f in range(1, faces + 1):
            ans += self.solve(n - 1, faces, total - f)
        return ans % self.MOD 

'''
Testcase
n = 30
faces = 41
total = 36
Your result
8347680
Expected
1623160

4 6 4
Your result
4
Expected
1
'''


'''
DP
T: O(100 * 100 * 100) = O(total  * faces * n)
S: O(100 * 100) = O(total * n)

Success!
Your code took 483 milliseconds — faster than 27.00% in Python
'''
class Solution:
    MOD = 10 ** 9 + 7

    def solve(self, n, faces, total):
        dp = [[0] * n for _ in range(total + 1)]
        for i in range(1, min(faces + 1, total)):
            dp[i][0] = 1
        for j in range(1, n):
            for t0 in range(total):
                for f in range(1, faces + 1):
                    if t0 + f <= total:
                        dp[t0 + f][j] += dp[t0][j - 1] % self.MOD
                    else:
                        break
        return dp[total][n - 1] % self.MOD

