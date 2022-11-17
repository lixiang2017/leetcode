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


'''
hash table + two pointers

Runtime: 1033 ms, faster than 34.60% of Python3 online submissions for Number of Matching Subsequences.
Memory Usage: 15.5 MB, less than 75.71% of Python3 online submissions for Number of Matching Subsequences.
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        # word -> bool
        memo = {}
        for word in words:
            if word in memo:
                ans += memo[word]
                continue
            else:
                it = iter(s)
                if all(ch in it for ch in word):
                    memo[word] = True
                    ans += 1
                else:
                    memo[word] = False
        return ans 



'''
Runtime: 927 ms, faster than 39.99% of Python3 online submissions for Number of Matching Subsequences.
Memory Usage: 15.1 MB, less than 98.90% of Python3 online submissions for Number of Matching Subsequences.
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @cache
        def isSubsequence(word):
            if len(word) > len(s):
                return False
            it = iter(s)
            return all(ch in it for ch in word)
        
        return sum(isSubsequence(w) for w in words)


'''
Runtime: 5979 ms, faster than 5.02% of Python3 online submissions for Number of Matching Subsequences.
Memory Usage: 15.5 MB, less than 75.71% of Python3 online submissions for Number of Matching Subsequences.
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @cache
        def isSubsequence(word):
            if len(word) > len(s):
                return False
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1 
            return i == len(word)
            
        return sum(isSubsequence(w) for w in words)
    

'''
执行用时：356 ms, 在所有 Python3 提交中击败了80.54% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了96.64% 的用户
通过测试用例：53 / 53
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(word):
            its = iter(s)
            return all(ch in its for ch in word)

        ans, cache = 0, dict()
        for w in words:
            if w not in cache:
                cache[w] = isSubsequence(w)
            ans += cache[w]
        return ans 
        