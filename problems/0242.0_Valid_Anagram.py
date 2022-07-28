'''
hash table

Runtime: 55 ms, faster than 85.13% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.5 MB, less than 66.69% of Python3 online submissions for Valid Anagram.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        