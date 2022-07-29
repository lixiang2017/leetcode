'''
hash table

Runtime: 66 ms, faster than 16.78% of Python3 online submissions for Find and Replace Pattern.
Memory Usage: 13.9 MB, less than 76.64% of Python3 online submissions for Find and Replace Pattern.
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [w for w in words if len(set(zip(w, pattern))) == len(set(list(w))) == len(set(list(pattern))) ]
