'''
approach: DFS + Cache / Recursion + Memoization
Time: O(target * N)
Space: O(target)

执行用时：52 ms, 在所有 Python3 提交中击败了54.81%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.57%的用户
'''


from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(target):
            if target < 0:
                return 0
            if 0 == target:
                return 1

            ans = 0
            for num in nums:
                ans += dfs(target - num)
            return ans

        return dfs(target)

'''
执行用时：44 ms, 在所有 Python3 提交中击败了90.69%的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了6.77%的用户
'''
from functools import cache, lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # @cache
        @lru_cache(maxsize=1005)
        def dfs(target):
            if target < 0:
                return 0
            if 0 == target:
                return 1

            ans = 0
            for num in nums:
                ans += dfs(target - num)
            return ans

        return dfs(target)


'''
approach: DP
Time: O(target * N)
Space: O(target)

执行用时：60 ms, 在所有 Python3 提交中击败22.22%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了61.59%的用户
'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]



