'''
approach: DFS / Recursion

You are here!
Your runtime beats 46.15 % of python3 submissions.
You are here!
Your memory usage beats 19.76 % of python3 submissions.
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(goal):
            if goal == 0:
                return 1
            if goal < 0:
                return 0
            ans = 0
            for num in nums:
                ans += dfs(goal - num)
            return ans
        
        return dfs(target)

    
'''
Your input
[1,2,3]
4
[4,2,1]
32
Your answer
7
39882198
Expected answer
7
39882198    
'''


'''
approach: DFS / Recursion

You are here!
Your runtime beats 96.94 % of python3 submissions.
You are here!
Your memory usage beats 19.18 % of python3 submissions.
'''

from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=1000)
        def dfs(goal):
            if goal == 0:
                return 1
            if goal < 0:
                return 0
            ans = 0
            for num in nums:
                ans += dfs(goal - num)
            return ans
        
        return dfs(target)



