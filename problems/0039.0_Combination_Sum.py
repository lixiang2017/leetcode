'''
DFS

Runtime: 74 ms, faster than 85.65% of Python3 online submissions for Combination Sum.
Memory Usage: 14.1 MB, less than 75.64% of Python3 online submissions for Combination Sum.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        n = len(candidates)
        
        def dfs(idx, remain, seq):
            if remain == 0:
                ans.append(seq)
            for i in range(idx, n):
                if candidates[i] > remain:
                    break
                dfs(i, remain - candidates[i], seq + [candidates[i]])
        
        dfs(0, target, [])
        return ans
        
