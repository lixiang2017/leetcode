'''
Runtime: 103 ms, faster than 89.18% of Python3 online submissions for Optimal Partition of String.
Memory Usage: 14.5 MB, less than 99.47% of Python3 online submissions for Optimal Partition of String.
'''
class Solution:
    def partitionString(self, s: str) -> int:
        ans, seen = 1, set()
        for ch in s:
            if ch in seen:
                ans += 1
                seen = {ch}
            else:
                seen.add(ch)
        return ans 

'''
Runtime: 165 ms, faster than 31.42% of Python3 online submissions for Optimal Partition of String.
Memory Usage: 14.6 MB, less than 90.81% of Python3 online submissions for Optimal Partition of String.
'''
class Solution:
    def partitionString(self, s: str) -> int:
        ans, mask = 1, 0
        for ch in s:
            m = 1 << (ord(ch) - ord('a'))
            if m & mask:
                ans += 1
                mask = m
            else:
                mask |= m
        return ans 
        