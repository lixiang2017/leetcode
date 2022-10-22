'''
sliding window


Runtime: 684 ms, faster than 13.18% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.8 MB, less than 36.77% of Python3 online submissions for Minimum Window Substring.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        hs, ht = defaultdict(int), defaultdict(int)
        for ch in t:
            ht[ch] += 1
        start, end = -inf, inf 
        i = j = 0
        
        def cover(hs, ht):
            for ch, cnt in ht.items():
                if hs[ch] < cnt:
                    return False
            return True
        
        while True:
            while j < m and not cover(hs, ht):
                hs[s[j]] += 1
                j += 1
            # [i, j)
            if not(j <= m and cover(hs, ht)):
                break 
            while i < j and cover(hs, ht):
                if end - start > j - i:
                    start, end = i, j
                if j - i == n:
                    return s[i: j]
                hs[s[i]] -= 1
                i += 1

        return '' if start == -inf else s[start: end]
    
