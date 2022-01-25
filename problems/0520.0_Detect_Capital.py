'''
Runtime: 45 ms, faster than 34.46% of Python3 online submissions for Detect Capital.
Memory Usage: 14.3 MB, less than 13.27% of Python3 online submissions for Detect Capital.
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
        