'''
hash table + two pointers

执行用时：392 ms, 在所有 Python3 提交中击败了59.09% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了62.12% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # word -> bool
        memo = dict()
        def isSubSequence(s: str, word: str) -> bool:
            if len(s) < len(word):
                return False
            it = iter(s)
            return all(need in it for need in word)
            
        ans = 0
        for word in words:
            if word not in memo:
                memo[word] = isSubSequence(s, word)
            ans += memo[word]
        return ans
