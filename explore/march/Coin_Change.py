'''
108 / 182 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[185,429,111,150,414,203,418]
8197
'''

import sys
class Solution:
    # fewestTotal = sys.maxint
    fewestTotal = sys.maxsize
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        coins.sort(reverse=True)
        coins = tuple(coins)  # TypeError: unhashable type: 'list'
        print (coins)
        self.dfs(amount, coins, 0, 0, N)
        return self.fewestTotal if self.fewestTotal != sys.maxsize else -1
    
    @cache
    def dfs(self, remainder, choices, total, idx, N):
        # print ('idx: ', idx)
        if remainder < 0:
            return 
        if remainder == 0:
            self.fewestTotal = min(self.fewestTotal, total)
        # cut branch
        if total >= self.fewestTotal:
            return 
        
        for i in range(idx, N):
            # choose
            self.dfs(remainder - choices[i], choices, total + 1, i, N)
            # not choose
            self.dfs(remainder, choices, total, i + 1, N)

'''
32 / 182 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[3,7,405,436]
8839
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        
        def dfs(remainder, idx):
            if remainder == 0:
                return 0
            total = float('inf')
            for i in range(idx, len(coins)):
                if remainder >= coins[i]:
                    total = min(total, dfs(remainder - coins[i], i) + 1)
            return total
        
        total = dfs(amount, 0)
        return total if total != float('inf') else -1



'''
use @cache in Python3
182 / 182 test cases passed.
Status: Accepted
Runtime: 3620 ms
Memory Usage: 384.2 MB
Submitted: 0 minutes ago
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        
        @cache
        def dfs(remainder, idx):
            if remainder == 0:
                return 0
            total = float('inf')
            for i in range(idx, len(coins)):
                if remainder >= coins[i]:
                    total = min(total, dfs(remainder - coins[i], i) + 1)
            return total
        
        total = dfs(amount, 0)
        return total if total != float('inf') else -1        







