'''
hash table
T: O(2N)
S: O(26)

Runtime: 193 ms, faster than 43.30% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.2 MB, less than 59.00% of Python3 online submissions for First Unique Character in a String.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i 
        return -1
