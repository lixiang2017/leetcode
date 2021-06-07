'''
59 / 138 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
[9,28,50,9,34,48,2,50,38,10,5,16,44,5,48,21,38,17,21,49]
20
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        self.ways = 0

        #@lru_cache(None) # will be wrong
        def dfs(i, N, cur, target):
            if i == N:
                if cur == target:
                    self.ways += 1
                return

            # add
            dfs(i + 1, N, cur + nums[i], target)
            # minus
            dfs(i + 1, N, cur - nums[i], target)
        
        dfs(0, N, 0, target)
        return self.ways


'''
DFS + @cache
Time: O(2^N)
Space: O(N)

执行用时：304 ms, 在所有 Python3 提交中击败了40.25% 的用户
内存消耗：46.1 MB, 在所有 Python3 提交中击败了5.04% 的用户
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        @cache
        def dfs(i, N, cur, target):
            if i == N:
                if cur == target:
                    return 1
                else:
                    return 0

            # add
            add = dfs(i + 1, N, cur + nums[i], target)
            # minus
            minus = dfs(i + 1, N, cur - nums[i], target)
            return add + minus
        
        return dfs(0, N, 0, target)
