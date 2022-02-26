'''
Runtime: 43 ms, faster than 56.73% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 62.82% of Python3 online submissions for Excel Sheet Column Number.
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for t in columnTitle:
            ans *= 26
            ans += ord(t) - ord('A') + 1
        return ans
    
        
        