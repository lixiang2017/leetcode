'''
DFS + cache

Runtime: 299 ms, faster than 52.23% of Python3 online submissions for Frog Jump.
Memory Usage: 33 MB, less than 22.87% of Python3 online submissions for Frog Jump.
'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if n < 2 or stones[0] != 0 or stones[1] != 1:
            return False
        pos2idx = {pos: i for i, pos in enumerate(stones)}
        
        
        @cache
        def dfs(idx, step):
            if idx == n - 1:
                return True
            
            cur = stones[idx]
            ret = False
            for next_step in [step - 1, step, step + 1]:
                if next_step > 0 and cur + next_step in pos2idx:
                    ret |= dfs(pos2idx[cur + next_step], next_step)
            return ret
        
        return dfs(1, 1)
