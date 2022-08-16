'''
hash set
T: O(26)
S: O(26)

Runtime: 47 ms, faster than 52.83% of Python3 online submissions for First Letter to Appear Twice.
Memory Usage: 13.8 MB, less than 51.74% of Python3 online submissions for First Letter to Appear Twice.
'''
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for ch in s:
            if ch in seen:
                return ch 
            seen.add(ch)
        return ''
