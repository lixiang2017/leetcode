'''
Runtime: 40 ms, faster than 90.84% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.4 MB, less than 97.19% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[:: -1] for word in s.split())
        