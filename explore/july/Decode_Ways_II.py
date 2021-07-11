'''
DFS

199 / 217 test cases passed.
	Status: Time Limit Exceeded
	
Submitted: 0 minutes ago
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        total = 0
        one = set(str(i) for i in range(1, 10))
        two = set(str(i) for i in range(10, 27))
        six = set(str(i) for i in range(7))
        nine = set(str(i) for i in range(7, 10))
        #one_two = set(str(i) for i in range(1, 27))
        N = len(s)
        
        @cache
        def dfs(i):
            if i >= N:
                return 1
            ans = 0
            # one
            if s[i] in one:
                ans += 1 * dfs(i + 1)
            elif s[i] == '*':
                ans += 9 * dfs(i + 1)
            
            # two
            if i + 1 < N:
                if s[i: i + 2] in two:
                    ans += 1 * dfs(i + 2)
                elif s[i: i + 2] == '**' : # [0-9]*   **   *[0-9] 
                    ans += 15 * dfs(i + 2)
                elif s[i] == '1' and s[i + 1] == '*':
                    ans += 9 * dfs(i + 2)
                elif s[i] == '2' and s[i + 1] == '*':
                    ans += 6 * dfs(i + 2)
                elif s[i] == '*' and s[i + 1] in six:
                    ans += 2 * dfs(i + 2)
                elif s[i] == '*' and s[i + 1] in nine:
                    ans += 1 * dfs(i + 2)
                    
            return ans
        
        total = dfs(0)
        return total % MOD


'''
217 / 217 test cases passed.
	Status: Accepted
Runtime: 632 ms
Memory Usage: 209.2 MB


You are here!
Your runtime beats 41.69 % of python3 submissions.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        total = 0
        one = set(str(i) for i in range(1, 10))
        two = set(str(i) for i in range(10, 27))
        six = set(str(i) for i in range(7))
        nine = set(str(i) for i in range(7, 10))
        #one_two = set(str(i) for i in range(1, 27))
        N = len(s)
        
        @cache
        def dfs(i):
            if i >= N:
                return 1
            ans = 0
            # one
            if s[i] in one:
                ans += 1 * dfs(i + 1)
            elif s[i] == '*':
                ans += 9 * dfs(i + 1)
            
            # two
            if i + 1 < N:
                if s[i: i + 2] in two:
                    ans += 1 * dfs(i + 2)
                elif s[i: i + 2] == '**' : # [0-9]*   **   *[0-9] 
                    ans += 15 * dfs(i + 2)
                elif s[i] == '1' and s[i + 1] == '*':
                    ans += 9 * dfs(i + 2)
                elif s[i] == '2' and s[i + 1] == '*':
                    ans += 6 * dfs(i + 2)
                elif s[i] == '*' and s[i + 1] in six:
                    ans += 2 * dfs(i + 2)
                elif s[i] == '*' and s[i + 1] in nine:
                    ans += 1 * dfs(i + 2)
                    
            return ans % MOD
        
        return dfs(0)
        