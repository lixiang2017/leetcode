'''
中心扩散法
T： O（N * （N + N）） = O（N^2)
S: O(1)

Runtime: 165 ms, faster than 61.40% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 13.9 MB, less than 75.82% of Python3 online submissions for Palindromic Substrings.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        for i in range(n):
            # odd
            step = 1
            # i - step ...i ... i + step
            while i - step >= 0 and i + step < n and s[i - step] == s[i + step]:
                step += 1
            ans += step
            
            # even
            step = 1
            # i - step + 1 ... i + step
            while i - step + 1 >= 0 and i + step < n and s[i - step + 1] == s[i + step]:
                step += 1            
            ans += step - 1
            
        return ans 
