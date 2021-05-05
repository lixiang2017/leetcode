'''
approach: Hash Table + Sort + DP
Time: O(N + NlogN + N)
Space: O(N + 2N) = O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了47.28% 的用户
'''

from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for num in nums:
            table[num] += num
        
        uniques = sorted(table.keys())
        N = len(uniques)
        dp = [[0] * 2 for _ in range(N)]
        for i in range(N):
            if 0 == i:
                # not take
                dp[0][0] = 0  # not earn
                # take
                dp[0][1] = table[uniques[0]] # earn
                continue
            
            if uniques[i] == uniques[i - 1] + 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) 
                dp[i][1] = dp[i - 1][0] + table[uniques[i]]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + table[uniques[i]]

        return max(dp[-1])
