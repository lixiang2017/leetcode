'''
bit mask + backtrack

Runtime: 132 ms, faster than 82.59% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
Memory Usage: 13.9 MB, less than 64.77% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def mask(s):
            m = 0
            for ch in s:
                b = 1 << (ord(ch) - ord('a'))
                if m & b:
                    return 0
                m |= b 
            return m
        
        masks = [m for s in arr if (m := mask(s)) != 0]
        n = len(masks)
        ans = 0
        def backtrack(i, now):
            nonlocal ans
            ans = max(ans, now.bit_count())
            if i == n:
                return 
            # use
            if now & masks[i] == 0:
                backtrack(i + 1, now | masks[i])
            # not use
            backtrack(i + 1, now)
            
        backtrack(0, 0)
        return ans 
    
