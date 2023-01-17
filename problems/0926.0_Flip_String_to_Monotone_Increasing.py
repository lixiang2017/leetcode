'''
accumulate sum, rolling to calculate the answer

Runtime: 375 ms, faster than 56.73% of Python3 online submissions for Flip String to Monotone Increasing.
Memory Usage: 14.9 MB, less than 72.76% of Python3 online submissions for Flip String to Monotone Increasing.
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        freq, n = Counter(s), len(s)
        ans = freq['0']
        one = 0
        for i, ch in enumerate(s):
            if ch == '1':
                one += 1
            # former 1s and latter 0s
            flip = one + (freq['0'] - (i + 1 - one))
            ans = min(ans, flip)
        return ans 
        
