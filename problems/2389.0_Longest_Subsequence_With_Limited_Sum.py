'''
offline

Runtime: 103 ms, faster than 96.80% of Python3 online submissions for Longest Subsequence With Limited Sum.
Memory Usage: 14.2 MB, less than 40.29% of Python3 online submissions for Longest Subsequence With Limited Sum.
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        j, n = 0, len(nums)
        t = 0
        m = len(queries)
        ans = [0] * m
        for i, q in sorted(enumerate(queries), key=lambda pair: pair[1]):
            while j < n and t + nums[j] <= q:
                t += nums[j]
                j += 1
            ans[i] = j
        
        return ans 
