'''
Runtime: 266 ms, faster than 52.97% of Python3 online submissions for Non-decreasing Subsequences.
Memory Usage: 27.1 MB, less than 5.00% of Python3 online submissions for Non-decreasing Subsequences.
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def backtrack(cur: List[int], i: int) -> None:
            if len(cur) >= 2:
                ans.append(cur)
            if i == n:
                return
            # choose
            if not cur or cur[-1] <= nums[i]:
                backtrack(cur + [nums[i]], i + 1)
            # not choose
            backtrack(cur, i + 1)
        
        backtrack([], 0)
        ans = set(tuple(arr) for arr in ans)
        return [list(arr) for arr in ans]
        
        