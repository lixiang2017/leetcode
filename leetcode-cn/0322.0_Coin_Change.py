'''
DP

执行用时：812 ms, 在所有 Python3 提交中击败了96.42% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了30.85% 的用户
通过测试用例：188 / 188
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i >= c else float('inf') for c in coins) + 1
        return dp[-1] if dp[-1] != float('inf') else -1

'''
DFS + memoization

执行用时：1112 ms, 在所有 Python3 提交中击败了87.78% 的用户
内存消耗：30.2 MB, 在所有 Python3 提交中击败了8.20% 的用户
通过测试用例：188 / 188
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(None)
        def helper(amount):
            if 0 == amount:
                return 0
            return min(helper(amount - c) if amount >= c else float('inf') for c in coins) + 1
        
        return ans if (ans := helper(amount)) != float('inf') else -1


'''
BFS
q.popleft()
q.append()

执行用时：424 ms, 在所有 Python3 提交中击败了99.14% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了17.21% 的用户
通过测试用例：188 / 188
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([amount])
        step = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                remainder = q.popleft()
                if 0 == remainder:
                    return step 
                for c in coins:
                    if remainder >= c and remainder - c not in visited:
                        visited.add(remainder - c)
                        q.append(remainder - c)
            step += 1
        return -1
        

'''
q.pop()
q.appendleft()

执行用时：424 ms, 在所有 Python3 提交中击败了99.14% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了18.40% 的用户
通过测试用例：188 / 188
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([amount])
        step = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                remainder = q.pop()
                if 0 == remainder:
                    return step 
                for c in coins:
                    if remainder >= c and remainder - c not in visited:
                        visited.add(remainder - c)
                        q.appendleft(remainder - c)
            step += 1
        return -1


'''
DP
完全背包问题, 无限数量

执行用时：1236 ms, 在所有 Python3 提交中击败了64.10% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了86.04% 的用户
通过测试用例：188 / 188
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            if c <= amount:
                dp[c] = 1
        
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
                    
        return dp[-1] if dp[-1] != float('inf') else -1




